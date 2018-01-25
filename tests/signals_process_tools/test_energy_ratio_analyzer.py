import pprint
import unittest
import numpy as np
from signals_process_tools.energy_ratio_analyzer import EnergyRatioAnalyzer
from signals_process_tools.fft_generator import FftGenerator
from signals_process_tools.sliding_windows_maker import SlidingWindowsMaker


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.mock_signals = [
            [1, 2, 3, 4],
            [5, 6, 7, 8]
        ]
        self.t = np.linspace(0, 1, 500)
        self.mock_analyze_signals = [np.sin(2 * np.pi * 100 * self.t) + 3 * np.sin(2 * np.pi * 30 * self.t)]
        sliding_windows_maker = SlidingWindowsMaker(
            window_size=100,
            interval=100
        )
        fft_generator = FftGenerator()
        self.energy_ration_analyzer = EnergyRatioAnalyzer(
            sliding_windows_maker=sliding_windows_maker,
            fft_generator=fft_generator
        )

    def test_generate_result(self):
        result = self.energy_ration_analyzer.generate_result(self.mock_signals)
        self.assertEqual(4,
                         result['0']['peak_energy']
                         )
        self.assertEqual(2.5,
                         result['0']['average_energy']
                         )
        self.assertAlmostEqual(1.6,
                               result['0']['p_a_ratio']
                               )

    def test_analyze(self):
        """
        Test analyze. If the signals has no noises,
        the ratio of the peak energy to the average energy shall be the same
        :return:
        """
        result = self.energy_ration_analyzer.analyze(
            self.mock_analyze_signals
        )
        p_a_ratio_one = np.around(result['0']['0']['p_a_ratio'])
        p_a_ratio_two = np.around(result['0']['1']['p_a_ratio'])
        self.assertEqual(
            p_a_ratio_one,
            p_a_ratio_two
        )
