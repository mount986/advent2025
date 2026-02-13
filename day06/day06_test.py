import unittest

from advent2025.day06 import day06
from pathlib import Path


class TestDay06(unittest.TestCase):
    def test_part1(self):
        script_location = Path(__file__).parent
        file_to_open = script_location / "test.dat"
        expected = 4277556
        actual = day06.part1(file_to_open)
        self.assertEqual(expected, actual)

    def test_part2(self):
        script_location = Path(__file__).parent
        file_to_open = script_location / "test.dat"
        expected = 3263827
        actual = day06.part2(file_to_open)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
