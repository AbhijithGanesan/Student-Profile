import unittest
from MyProgram import greet


class TestMyProgram(unittest.TestCase):
    def test_greet(self):
        self.assertEqual(greet(), "Hello from GitHub Actions!")


if __name__ == "__main__":
    unittest.main()
