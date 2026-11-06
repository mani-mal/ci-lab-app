"""String stats library used by ci-lab-app."""

import unittest


def word_count(text):
    """Count words separated by whitespace."""
    return len([w for w in text.split() if w])


def initials(name):
    """Initials of 'First Last' → 'F.L'."""
    parts = [p for p in name.split() if p]
    return ".".join(p[0].upper() for p in parts)


def initials_test_wrapper(name):
    return initials(name)


def slugify(title):
    out = []
    for ch in title.lower():
        if ch.isalnum():
            out.append(ch)
        else:
            out.append("-")
    slug = "".join(out)
    while "--" in slug:
        slug = slug.replace("--", "-")
    return slug.strip("-")


def reverse_words(text):
    return " ".join(reversed(text.split()))


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
