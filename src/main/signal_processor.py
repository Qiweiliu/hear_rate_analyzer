import pprint
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from auxiliary.data_manager import DataManager
from auxiliary.decoder import Decoder
from auxiliary.mixer import Mixer
from auxiliary.selector import Selector
from auxiliary.signal_processor_utility import SignalProcessorUtility
from signals_process_tools.arduino_filter import ArduinoFilter
from signals_process_tools.bandpass_filter import BandPassFilter
from signals_process_tools.fft_generator import FftGenerator
from signals_process_tools.rate_analyzer import RateAnalyzer
from signals_process_tools.sliding_windows_maker import SlidingWindowsMaker
from signals_process_tools.static_filter import StdStaticFilter
from signals_process_tools.window_adder import WindowAdder
from operator import add
from scipy import signal
import seaborn as sns


class SignalProcessor:
    def __init__(self, sample_rate, fft_generator,
                 sliding_windows_maker, bandpass_filter):
        self.sample_rate = sample_rate
        self.fft_generator = fft_generator
        self.sliding_windows_maker = sliding_windows_maker
        self.bandpass_filter = bandpass_filter
        self.accurate_windows_size = int(
            np.around(
                self.sample_rate / 0.01666666667)
        )

    def process(self, raw_signals):
        def save_to_dictionary(windows,
                               filtered_signals,
                               added_windows,
                               ffts,
                               heart_rates):
            result_dictionary = {}
            result_dictionary['windows'] = windows
            result_dictionary['added_windows'] = added_windows
            result_dictionary['filtered_signals'] = filtered_signals
            result_dictionary['ffts'] = ffts
            result_dictionary['heart_rates'] = heart_rates
            return result_dictionary

        def process_single_list(signals):
            windows = None
            filtered_signals = None
            added_windows = None
            ffts = None
            heart_rates = None

            # cutting window
            windows = self.sliding_windows_maker.get(signals)

            # filter frequencies
            filtered_signals = self.bandpass_filter.filter(windows)

            # add window
            window_adder = WindowAdder()
            added_windows = window_adder.add(filtered_signals)
            # added_windows = filtered_signals

            # fft
            ffts = self.fft_generator.generate(signals_sets=added_windows,
                                               size=self.accurate_windows_size
                                               )

            rate_analyzer = RateAnalyzer(
                amplitude_sets=ffts,
                sample_rate=self.sample_rate
            )
            heart_rates = np.around(rate_analyzer.get(), decimals=2)
            return save_to_dictionary(windows,
                                      filtered_signals, added_windows, ffts, heart_rates
                                      )

        # create the utility
        signal_processor_utility = SignalProcessorUtility(raw_signals)
        decoded_signals = signal_processor_utility.read()

        result = []
        for signals in decoded_signals:
            result.append(process_single_list(signals))

        return signal_processor_utility.pack(result)


def print_result(result_dictionary):
    plt.subplot(411)
    plt.plot(result_dictionary['windows'])
    plt.subplot(413)
    plt.plot(result_dictionary['added_windows'])
    plt.subplot(412)
    plt.plot(result_dictionary['filtered_signals'])
    plt.subplot(414)
    plt.plot(np.absolute(
        np.fft.fftfreq(
            len(result_dictionary['ffts']),
            1 / sample_rate) * 60),
        result_dictionary['ffts'])
    plt.show()
