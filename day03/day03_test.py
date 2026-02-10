import unittest
from pathlib import Path

from advent2025.day03 import day03


class TestDay03(unittest.TestCase):
    def test_part1(self):
        script_location = Path(__file__).parent
        file_to_open = script_location / "test.dat"
        expected = 357
        actual = day03.part1(file_to_open)
        self.assertEqual(expected, actual)

    def test_part2(self):
        script_location = Path(__file__).parent
        file_to_open = script_location / "test.dat"
        expected = 3121910778619
        actual = day03.part2(file_to_open)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
