#!/usr/bin/env python3
"""
Advanced Text Processing CLI Tool for Computational Linguistics.
Author: Rami Izzeddin
"""

import argparse
import re
from typing import Dict, List

class NLPTextAnalyzer:
    def __init__(self, text: str):
        self.raw_text = text

    def clean_text(self) -> str:
        """Removes HTML tags, extra whitespace, and standardizes text."""
        clean = re.sub(r'<[^>]+>', '', self.raw_text)
        clean = re.sub(r'\s+', ' ', clean)
        return clean.strip()

    def extract_stats(self) -> Dict[str, int]:
        """Calculates basic corpus statistics."""
        cleaned = self.clean_text()
        words = cleaned.split()
        sentences = re.split(r'[.!?]+', cleaned)
        sentences = [s for s in sentences if s.strip()]
        
        return {
            "total_characters": len(cleaned),
            "total_words": len(words),
            "total_sentences": len(sentences)
        }

def main():
    parser = argparse.ArgumentParser(description="NLP Text Normalizer and Stats Generator")
    parser.add_argument("-t", "--text", type=str, required=True, help="Input text string to process")
    args = parser.parse_args()

    analyzer = NLPTextAnalyzer(args.text)
    stats = analyzer.extract_stats()

    print("=== NLP Corpus Analysis Results ===")
    print(f"Cleaned Text : {analyzer.clean_text()}")
    print(f"Word Count   : {stats['total_words']}")
    print(f"Sentences    : {stats['total_sentences']}")
    print(f"Char Count   : {stats['total_characters']}")

if __name__ == "__main__":
    main()
