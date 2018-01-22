import unittest

from signals_process_tools.sliding_windows_maker import SlidingWindowsMaker


class TestSlidingWindowsMaker(unittest.TestCase):

    def setUp(self):
        self.mock_signals = [1, 2, 3, 4, 5]
        self.sliding_windows_maker = SlidingWindowsMaker(window_size=2,
                                                         interval=1)

    def test_get(self):
        result_one = self.sliding_windows_maker.get(self.mock_signals)

        self.assertEqual([1, 2], result_one[0])
        self.assertEqual([2, 3], result_one[1])
        self.assertEqual([3, 4], result_one[2])
        self.assertEqual([4, 5], result_one[3])

    def test_get_two(self):
        sliding_windows_maker = SlidingWindowsMaker(window_size=3,
                                                    interval=3)
        result_two = sliding_windows_maker.get([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])
        self.assertEqual(3, len(result_two))
        self.assertEqual([1, 2, 3], result_two[0])
        self.assertEqual([4, 5, 6], result_two[1])
        self.assertEqual([7, 8, 9], result_two[2])
