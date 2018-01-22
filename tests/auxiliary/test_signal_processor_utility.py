import pprint
import unittest

from auxiliary.signal_processor_utility import SignalProcessorUtility


class TestSignalProcessorUtility(unittest.TestCase):

    def setUp(self):
        self.mock_signals = {
            '1_11': {
                '87': [5, 6, 7],
                '22': [1, 2, 3]
            },
            '1_4': {
                '33': [5, 4, 7],
                '1': [2, 3, 4]
            },
            '1_7': {
                '44': [9, 4, 7],
                '98': [4, 5, 6]
            }
        }

        self.mock_pack_signals = [
            {
                'windows': [[5, 6, 7]],
                'added_windows': [[]],
                'filtered_signals': [[]],
                'ffts': [[]],
                'heart_rates': [[]]
            },
            {
                'windows': [[1, 2, 3]],
                'added_windows': [[]],
                'filtered_signals': [[]],
                'ffts': [[]],
                'heart_rates': [[]]
            },
            {
                'windows': [[1, 2, 3]],
                'added_windows': [[]],
                'filtered_signals': [[]],
                'ffts': [[]],
                'heart_rates': [[]]
            },
            {
                'windows': [[1, 2, 3]],
                'added_windows': [[]],
                'filtered_signals': [[]],
                'ffts': [[]],
                'heart_rates': [[]]
            },
            {
                'windows': [[1, 2, 3]],
                'added_windows': [[]],
                'filtered_signals': [[]],
                'ffts': [[]],
                'heart_rates': [[]]
            },
            {
                'windows': [[1, 2, 3]],
                'added_windows': [[]],
                'filtered_signals': [[]],
                'ffts': [[]],
                'heart_rates': [[]]
            }
        ]
        self.signal_processor_utility = SignalProcessorUtility(self.mock_signals)

    def test_read(self):
        result = self.signal_processor_utility.read()
        self.assertListEqual([
            [5, 6, 7], [1, 2, 3], [5, 4, 7], [2, 3, 4], [9, 4, 7], [4, 5, 6]
        ], result)

    def test_pack(self):
        result = self.signal_processor_utility.pack(self.mock_pack_signals)
        self.assertListEqual([5, 6, 7],
                             result['1_11']['87']['windows'][0]
                             )
        self.assertListEqual([1, 2, 3],
                             result['1_4']['33']['windows'][0]
                             )
