# tests/test_translator.py

import pytest
from morse_code_dict import morse_code_dict
from main import text_to_morse


def test_single_word():
    """Translates a single word"""
    assert text_to_morse("HELLO") == ".... . .-.. .-.. ---"


def test_sentence_with_space():
    """Translates multiple words"""
    result = text_to_morse("HELLO WORLD")
    assert result == ".... . .-.. .-.. --- / .-- --- .-. .-.. -.."


def test_with_punctuation():
    """Handles punctuation correctly"""
    result = text_to_morse("HELLO, WORLD!")
    expected = ".... . .-.. .-.. --- --..-- / .-- --- .-. .-.. -.. -.-.--"
    assert result == expected


def test_lowercase_input():
    """Converts lowercase input correctly"""
    assert text_to_morse("hello") == ".... . .-.. .-.. ---"


def test_unsupported_character():
    """Unknown symbols should remain unchanged"""
    result = text_to_morse("HELLO🙂")
    assert "🙂" in result