import pytest
from morse_coder import decode_morse


def test_decode_basic():
    assert decode_morse("... --- ...") == "SOS"


def test_decode_words_with_spaces():
    assert decode_morse(".... . .-.. .-.. ---   .-- --- .-. .-.. -..") == "HELLO WORLD"


def test_decode_words_with_slash():
    assert decode_morse(".... . .-.. .-.. --- / .-- --- .-. .-.. -..") == "HELLO WORLD"


def test_unknown_sequence():
    assert decode_morse("... --- ... -.-.-") == "SOS?"


def test_empty():
    assert decode_morse("") == ""


def test_typographic_apostrophe_normalization():
    # Input contains a typographic apostrophe (U+2019) inside a token; it
    # should be cleaned and decoded correctly
    assert decode_morse(".----. ..’ --") == "'IM"
