import numpy as np
from auxiliary.signal_processor_utility import SignalProcessorUtility
from signals_process_tools.energy_ratio_analyzer import EnergyRatioAnalyzer
from signals_process_tools.fft_generator import FftGenerator
from signals_process_tools.rate_analyzer import RateAnalyzer
from signals_process_tools.sliding_windows_maker import SlidingWindowsMaker
from signals_process_tools.window_adder import WindowAdder


class SignalProcessor:
    def __init__(self, fft_generator,
                 sliding_windows_maker, bandpass_filter, signal_processor_utility):
        self.fft_generator = fft_generator
        self.sliding_windows_maker = sliding_windows_maker
        self.bandpass_filter = bandpass_filter
        self.accurate_windows_size = 0
        self.signal_processor_utility = signal_processor_utility
        self.sample_rate = None

    def process(self, raw_signals, sample_rate):
        def save_to_dictionary(windows,
                               filtered_signals,
                               added_windows,
                               ffts,
                               heart_rates):
            result_dictionary = {'windows': windows,
                                 'added_windows': added_windows,
                                 'filtered_signals': filtered_signals,
                                 'ffts': ffts,
                                 'heart_rates': heart_rates}
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

        #
        self.sample_rate = sample_rate
        self.bandpass_filter.set_sample_rate(sample_rate)

        # compute accurate size
        self.accurate_windows_size = int(
            np.around(
                sample_rate / 0.01666666667)
        )

        # create the utility and read content from the dictionary
        self.signal_processor_utility.data = raw_signals
        decoded_signals = self.signal_processor_utility.read()

        result = []
        for signals in decoded_signals:
            result.append(process_single_list(signals))

        return self.signal_processor_utility.pack(result)
