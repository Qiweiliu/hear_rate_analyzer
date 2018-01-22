import unittest

import numpy as np

from signals_process_tools.fft_generator import FftGenerator
from signals_process_tools.rate_analyzer import RateAnalyzer


class TestRateAnalyzer(unittest.TestCase):

    def setUp(self):
        self.fft_generator = FftGenerator()
        self.t = np.linspace(0, 1, 500)
        self.mock_signals = [np.sin(2 * np.pi * 100 * self.t) + 3 * np.sin(2 * np.pi * 30 * self.t),
                             np.sin(2 * np.pi * 100 * self.t) + 3 * np.sin(2 * np.pi * 30 * self.t)]
        self.result = self.fft_generator.generate(self.mock_signals, 500)
        self.rate_analyzer = RateAnalyzer(amplitude_sets=self.result,
                                          sample_rate=500)

    def test_analyze(self):
        result = self.rate_analyzer.get()
        self.assertEqual(30 * 60, result[0])
        self.assertEqual(30 * 60, result[1])
