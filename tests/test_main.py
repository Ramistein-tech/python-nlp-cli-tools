#!/usr/bin/env python3
"""
Unit tests for TextProcessor class
"""

from main import TextProcessor

def test_normalize():
    processor = TextProcessor("  Test   NLP   Data  ")
    assert processor.normalize() == "Test NLP Data"

def test_count_words():
    processor = TextProcessor("One Two Three")
    assert processor.count_words() == 3
