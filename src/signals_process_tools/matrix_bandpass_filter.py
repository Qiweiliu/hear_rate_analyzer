from auxiliary.static_filter_utility import StaticFilterUtility
import numpy as np


class MatrixBandpassFilter:
    def __init__(self, bandpass_filter):
        self.bandpass_filter = bandpass_filter

    def filter(self, decoded_signals):
        # filter unwanted signals out of the target frequency range
        static_filter_utility = StaticFilterUtility(decoded_signals)

        i = 0
        signals = static_filter_utility.read()
        for key in decoded_signals.keys():
            decoded_signals[key] = np.array(
                self.bandpass_filter.filter(
                    signals[i].transpose()
                )
            ).transpose()
            i += 1
        return decoded_signals

    def filter_single_set(self, raw_signals):
        return np.array(
            self.bandpass_filter.filter(
                raw_signals.transpose()
            )
        ).transpose()
