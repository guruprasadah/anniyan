from anniyan import is_valid_mime


def test_valid_basic():
    assert is_valid_mime("application/json")
    assert is_valid_mime("text/html")
    assert is_valid_mime("image/png")


def test_invalid_basic():
    assert not is_valid_mime("application/not-real")
    assert not is_valid_mime("fake/type")
    assert not is_valid_mime("justastring")


def test_case_insensitivity():
    assert is_valid_mime("Application/JSON")
    assert is_valid_mime("TEXT/HTML")


def test_with_parameters():
    assert is_valid_mime("application/json; charset=utf-8")
    assert is_valid_mime("text/html; charset=UTF-8")


def test_missing_slash():
    assert not is_valid_mime("applicationjson")

def test_empty():
    assert not is_valid_mime("")

def test_weird_format():
    assert not is_valid_mime("/")
    assert not is_valid_mime("application/")
    assert not is_valid_mime("/json")

def test_wrong_domain():
    assert not is_valid_mime("image/json")

from anniyan.domains import domain_map

def test_all_generated_types_are_valid():
    for domain, subtypes in domain_map.items():
        for subtype in subtypes:
            assert is_valid_mime(f"{domain}/{subtype}")