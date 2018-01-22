import unittest

from auxiliary.static_filter_utility import StaticFilterUtility


class TestStaticFilterUtility(unittest.TestCase):
    def setUp(self):
        self.mock_signals = {
            '1_11': [
                [1], [2]
            ],
            '1_4': [
                [3], [4]
            ]
        }
        self.static_filter_utility = StaticFilterUtility(self.mock_signals)

    def test_read(self):
        result = self.static_filter_utility.read()
        self.assertListEqual(
            [[1], [2]], result[0]
        )
        self.assertListEqual(
            [[3], [4]], result[1]
        )

    def test_pack(self):
        mock_signals = [[(0, [1, 10])], [(0, [1, 10])]]
        result = self.static_filter_utility.pack(mock_signals)
        self.assertListEqual(
            [1, 10], result['1_11']['0']
        )
        self.assertListEqual(
            [1, 10], result['1_4']['0']
        )

    def test_pack_multiply_sub_indices(self):
        mock_signals = [[(0, [1, 10]), (1, [2, 3])], [(0, [1, 10]), (1, [2, 3])]]
        result = self.static_filter_utility.pack(mock_signals)
        self.assertListEqual(
            [1, 10], result['1_11']['0']
        )
        self.assertListEqual(
            [1, 10], result['1_4']['0']
        )
        self.assertListEqual(
            [2, 3], result['1_11']['1']
        )
        self.assertListEqual(
            [2, 3], result['1_4']['1']
        )
