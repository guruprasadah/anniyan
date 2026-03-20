# Anniyan

A fast, minimal, and IANA-compliant MIME type validator for Python.

---

## ✨ Features

- ✔️ Validates MIME types against official IANA registry
- ⚡ Zero runtime dependencies
- 🧠 Handles real-world inputs (`; charset=utf-8`, casing, etc.)
- 📦 Lightweight and fast (set-based lookup)
- 🔁 Deterministic, pre-generated data (no network at runtime)

---

## 📦 Installation

### Local development

```bash
pip install -e /path/to/anniyan
````

### From wheel

```bash
pip install dist/anniyan-0.1.0-py3-none-any.whl
```

---

## 🚀 Usage

```python
from anniyan import is_valid_mime

is_valid_mime("application/json")              # True
is_valid_mime("text/html; charset=UTF-8")      # True
is_valid_mime("image/not-real")                # False
```

---

## 🧪 Behavior

* Case-insensitive
* Ignores MIME parameters (`; charset=...`)
* Requires valid `type/subtype` structure

---

## 🏗️ How It Works

* MIME types are fetched from the official IANA registry
* Data is normalized and compiled into Python sets
* Validation is a constant-time lookup

---

## 🔧 Development

Install dev dependencies:

```bash
pip install .[dev]
```

Run tests:

```bash
pytest
```

Regenerate MIME dataset:

```bash
python -m anniyan.data_generator
```

---

## 📄 License

MIT
