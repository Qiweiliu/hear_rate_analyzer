import numpy as np


class RateAnalyzer:
    """
    Get the maximum frequency of the input fft amplitudes
    and find the max frequency that will be converted to BPM later
    """

    def __init__(self, amplitude_sets, sample_rate):
        self.sample_rate = sample_rate
        self.amplitudes_sets = amplitude_sets

    def get(self):
        results = []
        for amplitudes in self.amplitudes_sets:
            results.append(
                self.find_max(amplitudes) * 60
            )
        return results

    def _compare_indices(self, frequency_array):
        """
        Select the max candidate frequency
        :param frequency_array: A list of candidate frequencies
        :return: Max frequency
        """
        frequency_array = np.absolute(frequency_array)
        max_frequency = np.max(frequency_array)
        return max_frequency

    def find_max(self, amplitudes):
        """
        Find the max amplitudes and its corresponding index
        .warn:: the received signals shall be list rather than a numpy array
        :param amplitudes: amplitudes from fft
        :return: A tail call to select the max frequency
        """
        max_amplitude_index = np.where(amplitudes == np.max(amplitudes))

        matched_frequency = np.fft.fftfreq(
            len(amplitudes),
            1 / self.sample_rate)[max_amplitude_index]
        return self._compare_indices(matched_frequency)
