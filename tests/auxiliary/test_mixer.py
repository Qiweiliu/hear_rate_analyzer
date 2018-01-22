import unittest

from auxiliary.mixer import Mixer


class TestMixer(unittest.TestCase):

    def setUp(self):
        self.mock_signals = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        self.mixer = Mixer()

    def test_mix(self):
        result = self.mixer.mix(self.mock_signals)
        self.assertListEqual(result.tolist(),
                             [12, 15, 18]
                             )
