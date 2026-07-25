import unittest

from stringutils import is_palindrome, reverse_words


class TestIsPalindrome(unittest.TestCase):
    def test_simple_palindrome(self):
        self.assertTrue(is_palindrome("racecar"))

    def test_phrase_with_spaces_and_case(self):
        self.assertTrue(is_palindrome("Was it a car or a cat I saw"))

    def test_non_palindrome(self):
        self.assertFalse(is_palindrome("hello"))


class TestReverseWords(unittest.TestCase):
    def test_reverses_word_order(self):
        self.assertEqual(reverse_words("hello world"), "world hello")

    def test_single_word_unchanged(self):
        self.assertEqual(reverse_words("hello"), "hello")

    def test_empty_string(self):
        self.assertEqual(reverse_words(""), "")


if __name__ == "__main__":
    unittest.main()
