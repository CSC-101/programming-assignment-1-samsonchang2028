import data
import hw1
import unittest


# Write your test cases for each part below.

class TestCases(unittest.TestCase):
    # Part 1
    def test_vowel_count_1(self):
        words = 'String'
        results = hw1.vowel_count(words)
        expected = 1
        self.assertEqual(expected, results)

    # Part 2
    def test_short_lists1(self):
        values = [[1,2],[3],[4,5,6],[7,8]]
        results = hw1.short_lists(values)
        expected = [[1,2],[7,8]]
        self.assertEqual(expected, results)

    # Part 3
    def test_ascending_pairs_1(self):
        values = [[1,2],[3],[4,5,6],[10,9]]
        results = hw1.ascending_pairs(values)
        expected = [[1, 2], [9, 10]]
        self.assertEqual(expected, results)

    # Part 4


    # Part 5


    # Part 6


    # Part 7


    # Part 8





if __name__ == '__main__':
    unittest.main()
