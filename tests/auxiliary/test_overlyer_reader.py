import unittest
import numpy as np

from auxiliary.overly_reader import OverlyReader


class TestOverlyReader(unittest.TestCase):

    def setUp(self):
        self.mock_signals = {
            '1_4': {
                '1': np.array([1, 2, 3]),
                '2': np.array([4, 5, 6])
            },
            '1_7': {
                '3': np.array([7, 8, 9]),
                '4': np.array([10, 11, 12])
            }
        }

        self.mock_pack_signals = [
            {'windows': np.array([5, 7, 9]),
             'added_windows': None,
             'filtered_signals': None,
             'ffts': None,
             'heart_rates': None},
            {'windows': np.array([17, 19, 21]),
             'added_windows': None,
             'filtered_signals': None,
             'ffts': None,
             'heart_rates': None}
        ]
        self.energy_overlyer = OverlyReader()

    def test_read(self):
        self.energy_overlyer.data = self.mock_signals
        result = self.energy_overlyer.read()
        self.assertListEqual(
            [5, 7, 9],
            result[0].tolist()
        )

    def test_pack(self):
        """
        The result shall be:
        self.mock_pack_signals = {
            '1_4': {'windows': [5, 7, 9],
                    'added_windows': None,
                    'filtered_signals': None,
                    'ffts': None,
                    'heart_rates': None},
            '1_7': {'windows': [17, 19, 21],
                    'added_windows': None,
                    'filtered_signals': None,
                    'ffts': None,
                    'heart_rates': None}
        }
        """
        self.energy_overlyer.data = self.mock_signals
        result = self.energy_overlyer.pack(self.mock_pack_signals)
        self.assertListEqual(
            [5, 7, 9],
            result['1_4']['windows'].tolist()
        )
        self.assertListEqual(
            [17, 19, 21],
            result['1_7']['windows'].tolist()
        )
