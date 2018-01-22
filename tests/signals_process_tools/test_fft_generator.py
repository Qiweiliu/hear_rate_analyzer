import unittest
import numpy as np

from signals_process_tools.fft_generator import FftGenerator


class TestFftGenerator(unittest.TestCase):
    def setUp(self):
        self.t = np.linspace(0, 1, 500)
        self.mock_signals = np.sin(2 * np.pi * 100 * self.t) + 3 * np.sin(2 * np.pi * 30 * self.t)
        self.fft_generator = FftGenerator()

    def test_generate(self):
        result = self.fft_generator.generate([self.mock_signals], len(self.mock_signals))
        self.assertEqual(len(result[0]), 500)
