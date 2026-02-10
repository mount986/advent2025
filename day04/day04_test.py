import unittest
from pathlib import Path

from advent2025.day04 import day04


class TestDay04(unittest.TestCase):
    def test_part1(self):
        script_location = Path(__file__).parent
        file_to_open = script_location / "test.dat"
        expected = 13
        actual = day04.part1(file_to_open)
        self.assertEqual(expected, actual)

    def test_part2(self):
        script_location = Path(__file__).parent
        file_to_open = script_location / "test.dat"
        expected = 43
        actual = day04.part2(file_to_open)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
