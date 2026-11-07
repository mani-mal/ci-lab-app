"""The CI script check, as a test command."""

import subprocess
import unittest


class ScriptCheckTest(unittest.TestCase):
    def test_hello_script_exits_zero(self):
        proc = subprocess.run(
            ["./scripts/hello.sh"], capture_output=True, text=True, timeout=30
        )
        self.assertEqual(proc.returncode, 0, proc.stdout + proc.stderr)


if __name__ == "__main__":
    unittest.main()
