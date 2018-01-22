import unittest

from signals_process_tools.arduino_filter import ArduinoFilter
from signals_process_tools.sliding_windows_maker import SlidingWindowsMaker


class TestArduinoFilter(unittest.TestCase):
    def setUp(self):
        self.mock_values = [[1], [2], [3], [4], [5], [6], [7], [8], [9], [0]]
        self.arduino_filter = ArduinoFilter()

        average_window_size = len(self.mock_values) // 5

        sliding_windows_maker = SlidingWindowsMaker(
            window_size=average_window_size,
            interval=average_window_size
        )
        self.output_values = sliding_windows_maker.get(
            self.mock_values
        )

        self.filtered_values = self.arduino_filter.reduce(
            self.output_values
        )

    def test_generate(self):
        self.assertEqual(
            1.5,
            self.filtered_values[0]
        )

        self.assertEqual(
            3.5,
            self.filtered_values[1]
        )

        self.assertEqual(
            5.5,
            self.filtered_values[2]
        )

    def test_filter_head(self):
        filtered_values = self.arduino_filter.filter_head(
            values=self.output_values,
            extend=2
        )
        print(filtered_values)
        self.assertEqual([[[None], [None]], [[None], [None]], [[5], [6]], [[7], [8]], [[9], [0]]],
                         filtered_values
                         )

    def test_filter_zeros(self):
        mock_values = [[[0], [0]], [[0], [1]], [[5], [6]], [[7], [8]], [[9], [0]]]
        filtered_values = self.arduino_filter.filter_zeros(
            mock_values
        )

        self.assertEqual(
            [[[[0], [1]], [[5], [6]], [[7], [8]], [[9], [0]]]],
            filtered_values
        )
