# Python NLP CLI Tools

![Python Version](https://img.shields.io/badge/python-3.11+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![License](https://img.shields.io/badge/license-MIT-green?style=for-the-badge)

A modular, extensible Command-Line Interface (CLI) application built in Python for automated natural language processing, linguistic tokenization, Part-of-Speech (POS) tagging, and regex text normalization.

---

## 🚀 Features

* **Tokenization & Lemmatization:** High-performance tokenization for text corpora using `spaCy` and `NLTK`.
* **POS Tagging:** Sentence-level Part-of-Speech tagging with structured outputs.
* **Regex Data Normalization:** Standardizes whitespace and extracts targeted textual entities.

---

## 💻 Usage Example

```python
import re

def clean_text(raw_text: str) -> str:
    """Removes special characters and extra whitespace from raw text."""
    text = re.sub(r'\s+', ' ', raw_text)
    return text.strip()

sample = "  Digital   Humanities  &   Python  Automation  "
print(clean_text(sample))
