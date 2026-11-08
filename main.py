#!/usr/bin/env python3
"""
Python NLP CLI Tools - Text Normalizer & Processor
Author: Rami Izzeddin
"""

import re

class TextProcessor:
    def __init__(self, text: str):
        self.text = text

    def normalize(self) -> str:
        """Standardize spaces and clean raw text input."""
        cleaned = re.sub(r'\s+', ' ', self.text)
        return cleaned.strip()

    def count_words(self) -> int:
        """Return total word count."""
        words = self.normalize().split()
        return len(words)

if __name__ == "__main__":
    sample_text = "   Welcome to   Digital Humanities NLP   Tools!   "
    processor = TextProcessor(sample_text)
    
    print(f"Original Text: '{sample_text}'")
    print(f"Normalized Text: '{processor.normalize()}'")
    print(f"Word Count: {processor.count_words()}")
