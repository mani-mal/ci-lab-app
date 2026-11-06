"""A test that fails about half the time (time-based)."""

import unittest


class FlakyTest(unittest.TestCase):
    def test_sometimes_fails(self):
        # Fails when the current second is odd: about half the time.
        import time

        second = int(time.time()) % 2
        self.assertEqual(second, 0, f"flaky failure: second={second}")


if __name__ == "__main__":
    unittest.main()
