import unittest
import numpy as np
from signals_process_tools.bandpass_filter import BandPassFilter
from signals_process_tools.rate_analyzer import RateAnalyzer


class TestBandPassFilter(unittest.TestCase):

    def setUp(self):
        self.t = np.linspace(0, 1, 500)
        self.mock_signals = [np.sin(2 * np.pi * 100 * self.t) + 3 * np.sin(2 * np.pi * 30 * self.t),
                             np.sin(2 * np.pi * 100 * self.t) + 3 * np.sin(2 * np.pi * 30 * self.t)]
        self.bandpass_filter = BandPassFilter(lowcut=20,
                                              highcut=40,
                                              frequency=500,
                                              order=5)
        # self.max_frequency_finder = RateAnalyzer()

    # def test_filter(self):
    #     """
    #     Test two outputs of the bandpass filter
    #     """
    #     result = self.bandpass_filter.filter(self.mock_signals)
    #     max_frequency_one = self.max_frequency_finder.get(
    #         amplitudes=np.absolute(
    #             np.fft.fft(result[0])),
    #         sample_rate=500)
    #     max_frequency_two = self.max_frequency_finder.get(
    #         amplitudes=np.absolute(
    #             np.fft.fft(result[1])),
    #         sample_rate=500)
    #     self.assertEqual(30, max_frequency_one)
    #     self.assertEqual(30, max_frequency_two)
