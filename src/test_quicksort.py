import unittest
from quicksort import quicksort


class TestQuicksort(unittest.TestCase):
    def test_sort(self):
        lst = [3, 7, 2, 8, 4, 6, 9, 1, 4]
        expected = [1, 2, 3, 4, 4, 6, 7, 8, 9]
        self.assertEqual(quicksort(lst), expected)


if __name__ == "__main__":
    unittest.main()