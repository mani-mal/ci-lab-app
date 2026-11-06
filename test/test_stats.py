"""Tests for the string stats library."""

import unittest

from stats import initials, reverse_words, slugify, word_count


class StatsTest(unittest.TestCase):
    def test_word_count(self):
        self.assertEqual(word_count("one two  three"), 3)

    def test_initials(self):
        self.assertEqual(initials("Ada  Lovelace"), "A.L")

    def test_slugify(self):
        self.assertEqual(slugify("Hello, World!"), "hello-world")

    def test_reverse_words(self):
        self.assertEqual(reverse_words("one two three"), "three two one")


if __name__ == "__main__":
    unittest.main()
