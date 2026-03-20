import asyncio
import aiohttp
import csv
import io
import pathlib


OUTPUT_DIR = pathlib.Path(__file__).parent



IANA_URL = "https://www.iana.org/assignments/media-types/"
IANA_DOMAINS = ["application",
                "audio",
                "font",
                "haptics",
                "image",
                "message",
                "model",
                "multipart",
                "text",
                "video"]

async def fetch_domain(session: aiohttp.ClientSession, domain: str):
    url = f"{IANA_URL}{domain}.csv"
    async with session.get(url, timeout=10) as response:
        text = await response.text()
        parsed = csv.reader(io.StringIO(text), delimiter=",")
        next(parsed, None)
        result = []
        for row in parsed:
            if len(row) > 1 and "/" in row[1]:
                result.append(row[1].split("/", 1)[1].lower())
        print(f"RETRIEVED {domain}")
        return domain, result

async def fetch_data():
    data: dict[str, list[str]] = {}

    async with aiohttp.ClientSession() as session:
        tasks = [fetch_domain(session, domain) for domain in IANA_DOMAINS]
        results = await asyncio.gather(*tasks)

    for domain, values in results:
        data[domain] = values

    return data


def create_final_file(data: dict[str, list[str]]):
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    with open(op_file := (OUTPUT_DIR / ("domains.py")), "w", encoding="utf-8") as f:
        f.write("# Auto-generated file. Do not edit.\n\n")
        f.write("domain_map: dict[str, set[str]] = dict()\n")
        for domain in data:
            f.write(f"{domain}: set[str] = {{\n\t")
            f.write(",\n\t".join([f'"{x}"' for x in data[domain]]))
            f.write("\n}\n")
            f.write(f'domain_map["{domain}"] = {domain}\n')
        print(f"Wrote to {str(op_file)}")


def main():
    print("Generating data...")
    data = asyncio.run(fetch_data())
    create_final_file(data)


if __name__ == "__main__":
    main()