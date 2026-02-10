import unittest
from pathlib import Path

from advent2025.day02 import day02


class TestDay01(unittest.TestCase):
    def test_part1(self):
        script_location = Path(__file__).parent
        file_to_open = script_location / "test.dat"
        expected = 1227775554
        actual = day02.part1(file_to_open)
        self.assertEqual(expected, actual)

    def test_part2(self):
        script_location = Path(__file__).parent
        file_to_open = script_location / "test.dat"
        expected = 4174379265
        actual = day02.part2(file_to_open)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
