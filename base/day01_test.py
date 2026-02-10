import unittest

from advent2025.day01 import day01
from pathlib import Path


class TestDay01(unittest.TestCase):
    def test_part1(self):
        script_location = Path(__file__).parent
        file_to_open = script_location / "test.dat"
        expected = 0
        actual = day01.part1(file_to_open)
        self.assertEqual(expected, actual)

    def test_part2(self):
        script_location = Path(__file__).parent
        file_to_open = script_location / "test.dat"
        expected = 0
        actual = day01.part1(file_to_open)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
