import unittest

from auxiliary.selector import Selector


class TestSelector(unittest.TestCase):

    def setUp(self):
        self.mock_dictionary = {
            '1_14': {
                '1': {
                    'windows': [[1, 2, 3]],
                    'added_windows': [[]],
                    'filtered_signals': [[]],
                    'ffts': [[9, 8, 3], [3, 3, 3]],
                    'heart_rates': [[]]
                }

            },
            '1_17': {
                '0': {
                    'windows': [[4, 5, 6]],
                    'added_windows': [[]],
                    'filtered_signals': [[]],
                    'ffts': [[7, 8, 9], [4, 4, 4]],
                    'heart_rates': [[]]
                },
                '4': {
                    'windows': [[4, 5, 6]],
                    'added_windows': [[]],
                    'filtered_signals': [[]],
                    'ffts': [[6, 6, 6], [5, 5, 5]],
                    'heart_rates': [[]]
                }

            }
        }
        self.selector = Selector(self.mock_dictionary)

    def test_select_all_ffts(self):
        result = self.selector.select_all_ffts(
            number=0)

        self.assertListEqual(
            result,
            [[9, 8, 3], [7, 8, 9], [6, 6, 6]]
        )

        result = self.selector.select_all_ffts(
            number=1)

        self.assertListEqual(
            result,
            [[3, 3, 3], [4, 4, 4], [5, 5, 5]]
        )

    def test_select_antenna_pairs(self):
        result = self.selector.select_antenna_pairs(
            ['1_14', '1_17'],
            0
        )
        self.assertListEqual(
            result,
            [[9, 8, 3], [7, 8, 9], [6, 6, 6]]
        )
