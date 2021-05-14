import unittest
from unittest.mock import patch
import word_count
class test_count(unittest.TestCase):

    def test_one(self):
        with patch('builtins.input', side_effect = "Hello"):
            output = word_count.wordCount()
        self.assertEqual(output, 1)
    def test_fail(self):
        with patch('builtins.input', side_effect = "Hello world"):
            output = word_count.wordCount()
        self.assertEqual(output, 1)
    def test_five(self):
        with patch('builtins.input', side_effect = "Hello world goodbye today tomorrow"):
            output = word_count.wordCount()
        self.assertEqual(output, 5)
    def test_empty(self):
        with patch('builtins.input', side_effect = None):
            output = word_count.wordCount()
        self.assertEqual(output, 0)


if __name__ == "__main__":
    unittest.main()