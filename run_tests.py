"""Small unittest runner for the morse coder (fallback when pytest isn't available)."""
import unittest

from morse_coder import decode_morse


class TestMorse(unittest.TestCase):
    def test_decode_basic(self):
        self.assertEqual(decode_morse("... --- ..."), "SOS")

    def test_decode_words_with_spaces(self):
        self.assertEqual(decode_morse(".... . .-.. .-.. ---   .-- --- .-. .-.. -.."), "HELLO WORLD")

    def test_decode_words_with_slash(self):
        self.assertEqual(decode_morse(".... . .-.. .-.. --- / .-- --- .-. .-.. -.."), "HELLO WORLD")

    def test_unknown_sequence(self):
        self.assertEqual(decode_morse("... --- ... -.-.-"), "SOS?")

    def test_empty(self):
        self.assertEqual(decode_morse("") , "")


if __name__ == "__main__":
    unittest.main()
