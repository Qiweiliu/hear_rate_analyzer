import unittest

from auxiliary.data_manager import DataManager
from main.signal_processor import SignalProcessor
from signals_process_tools.bandpass_filter import BandPassFilter
from signals_process_tools.fft_generator import FftGenerator
from signals_process_tools.sliding_windows_maker import SlidingWindowsMaker
from signals_process_tools.static_filter import StdStaticFilter
import numpy as np


class TestSignalProcessor(unittest.TestCase):
    def setUp(self):
        self.raw_signals = {'1_11': {'1': [2, 10], '0': [1, 10]}, '1_4': {'1': [2, 10], '0': [1, 10]}}
        sample_rate = 100
        fft_generator = FftGenerator()
        sliding_windows_maker = SlidingWindowsMaker(
            window_size=1,
            interval=1
        )

        # 0.866, 3.333
        bandpass_filter = BandPassFilter(
            lowcut=0.866,
            highcut=3.333,
            frequency=sample_rate,
            order=5
        )

        # set up signal processor
        self.signal_processor = SignalProcessor(
            sample_rate, fft_generator, sliding_windows_maker,
            bandpass_filter
        )

    def test_process(self):
        result = self.signal_processor.process(self.raw_signals)
        self.assertListEqual([[2. + 0.j], [10. + 0.j]],
                             result['1_11']['1']['ffts']
                             )
        self.assertListEqual([[1. + 0.j], [10. + 0.j]],
                             result['1_4']['0']['ffts']
                             )
