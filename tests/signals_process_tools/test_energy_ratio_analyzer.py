import pprint
import unittest
import numpy as np
from signals_process_tools.energy_ratio_analyzer import EnergyRatioAnalyzer
from signals_process_tools.fft_generator import FftGenerator
from signals_process_tools.sliding_windows_maker import SlidingWindowsMaker
import matplotlib.pyplot as plt

class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.t = np.linspace(0, 1, 500)
        self.noise_component = np.append(np.random.normal(0, 1, 100), [0] * 400)
        self.mock_analyze_signals = [np.sin(2 * np.pi * 100 * self.t) + 3 * np.sin(2 * np.pi * 30 * self.t),
                                     np.sin(2 * np.pi * 100 * self.t) + 3 * np.sin(2 * np.pi * 30 * self.t)]
        self.mock_noised_signals = [np.sin(2 * np.pi * 100 * self.t) + 3 * np.sin(2 * np.pi * 30 * self.t)
                                    +
                                    self.noise_component,
                                    np.sin(2 * np.pi * 100 * self.t) + 3 * np.sin(2 * np.pi * 30 * self.t)
                                    +
                                    self.noise_component
                                    ]

        self.sliding_windows_maker = SlidingWindowsMaker(
            window_size=100,
            interval=100
        )
        self.fft_generator = FftGenerator()
        self.energy_ration_analyzer = EnergyRatioAnalyzer(
            sliding_windows_maker=self.sliding_windows_maker,
            fft_generator=self.fft_generator,
            proportion=15
        )

    def test_temp(self):
        plt.plot(np.sin(2 * np.pi * 100 * self.t) + 3 * np.sin(2 * np.pi * 30 * self.t))
        plt.show()
        plt.plot(np.absolute(
            np.fft.fft(np.sin(2 * np.pi * 100 * self.t) + 3 * np.sin(2 * np.pi * 30 * self.t)
                       )
        )
        )
        plt.show()
        plt.plot(np.sin(2 * np.pi * 100 * self.t) + 3 * np.sin(2 * np.pi * 30 * self.t)
                 +
                 self.noise_component)
        plt.show()
        plt.plot(np.absolute(
            np.fft.fft(np.sin(2 * np.pi * 100 * self.t) + 3 * np.sin(2 * np.pi * 30 * self.t) + self.noise_component
                       )
        )
        )
        plt.show()

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

        p_a_ratio_one = np.around(result['1']['0']['p_a_ratio'])
        p_a_ratio_two = np.around(result['1']['1']['p_a_ratio'])
        self.assertEqual(
            p_a_ratio_one,
            p_a_ratio_two
        )

    def test_analyze_noised_signals(self):
        result = self.energy_ration_analyzer.analyze(
            self.mock_noised_signals
        )

    def test_remove(self):
        expected_value = np.array([0] * 100, dtype=complex)
        for i in range(100, 500, 100):
            expected_value += np.absolute(
                np.fft.fft(
                    self.mock_noised_signals[0]
                    [
                    i:
                    i + 100
                    ],
                    100
                )
            )

        # the proportion is set to 15 to eliminate the low power ration spectrum
        result = self.energy_ration_analyzer.remove(signals_sets=self.mock_noised_signals)
        # Only call tolist() method can enable the comparision function of the unittest
        self.assertListEqual(
            expected_value.tolist(),
            result[0].tolist()
        )
