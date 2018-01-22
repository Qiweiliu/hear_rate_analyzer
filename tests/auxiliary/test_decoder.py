import unittest

from auxiliary.decoder import Decoder


class TestDecoder(unittest.TestCase):
    def setUp(self):
        # Todo: The mock format is wrong actually!!!
        self.mock_signals = [
            [1, 11, 1, 7, 1, 4],
            [1, 2, 3, 4, 5, 6],
            [1, 2, 3, 4, 5, 6],
            [1, 2, 3, 4, 5, 6],
            [1, 2, 3, 4, 5, 6]
        ]
        self.decoder = Decoder(self.mock_signals)

    def test_decode(self):
        result = self.decoder.decode()
        self.assertListEqual(result['1_11'].tolist(),
                             [
                                 [1, 2],
                                 [1, 2],
                                 [1, 2],
                                 [1, 2],
                             ]
                             )
        self.assertListEqual(result['1_7'].tolist(),
                             [
                                 [3, 4],
                                 [3, 4],
                                 [3, 4],
                                 [3, 4],
                             ]
                             )
        self.assertListEqual(result['1_4'].tolist(),
                             [
                                 [5, 6],
                                 [5, 6],
                                 [5, 6],
                                 [5, 6],
                             ]
                             )

    def test_read_antenna_pairs(self):
        antenna_pairs = self.decoder.read_antenna_pairs()
        self.assertEqual(
            antenna_pairs[0],
            (1, 11)
        )
        self.assertEqual(
            antenna_pairs[1],
            (1, 7)
        )
        self.assertEqual(
            antenna_pairs[2],
            (1, 4)
        )
