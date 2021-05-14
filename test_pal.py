import unittest
from unittest.mock import patch
import palindrome

class test_pal(unittest.TestCase):
    def test_yes(self):
        with patch('builtins.input', side_effect = "racecar"):
            output = palindrome.check_pal()
        self.assertEqual(output, "yes")
    def test_no(self):
        with patch('builtins.input', side_effect = "goodbye"):
            output = palindrome.check_pal()
        self.assertEqual(output, "yes")
    def test_empty(self):
        with patch('builtins.input', side_effect =''):
            output = palindrome.check_pal()
        self.assertEqual(output, "empty")
    

if __name__ == "__main__":
    unittest.main()