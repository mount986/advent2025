import unittest

from advent2025.day01 import day01


class TestDay01(unittest.TestCase):
    def test_part1(self):
        expected = 3
        actual = day01.part1("test.dat")
        self.assertEqual(expected, actual)

    def test_part2(self):
        expected = 6
        actual = day01.part2("test.dat")
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
