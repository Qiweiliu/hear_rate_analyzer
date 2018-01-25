import numpy as np


class EnergyRatioAnalyzer:
    """
    An energy ratio analyzer to divide a time series signals and divides it into different section.
    To calculate the maximum, average, and ratio.
    """

    def __init__(self, sliding_windows_maker, fft_generator, proportion):
        self.sliding_windows_maker = sliding_windows_maker
        self.fft_generator = fft_generator
        self.single_window_size = self.sliding_windows_maker.window_size
        self.proportion = proportion

    def set_fft_window_size(self, fft_window_size):
        self.single_window_size = fft_window_size

    def analyze(self, signal_sets):
        """
        To analyze the signals sets
        :param signal_sets: A list of signals. i.e. [[1, 2, 3], [4, 5, 6]]
        :return: Return a dictionary that is automatically arranged by increasing order
        """
        i = 0
        result = {}
        for signals in signal_sets:
            windows = self.sliding_windows_maker.get(signals)
            result[str(i)] = self.generate_result(windows)
            i += 1
        return result

    def generate_result(self, windows):
        """
        :param windows:
        :return:
        """
        # TODO: The ffts size may have effects
        ffts = self.fft_generator.generate(windows, self.single_window_size)
        result = {}
        i = 0
        for fft_result in ffts:
            maximum = np.max(fft_result)
            mean = np.mean(fft_result)

            # only remain two significant figures. The order is chosen empirically
            ratio = np.round(maximum / mean, 3)
            result[str(i)] = {
                'peak_energy':
                    maximum,
                'average_energy':
                    mean,
                'p_a_ratio':
                    ratio,
                'signals':
                    fft_result
            }
            i += 1
        return result

    def remove(self, signals_sets):
        """
        Remove the section of signals that below the the standard
        ..warning: The data type of ffts shall be always converted to real number！！！
        :param signals_sets:
        :param proportion: calculated from peak_energy / average_energy
        :return: return a list that contain ffts corresponding to the input signal_sets
        """
        result_dictionary = self.analyze(signals_sets)
        result = []
        for index, attributes in result_dictionary.items():

            # The partial_result shall be cleared after the addition process
            partial_result = np.array([0] * self.single_window_size, dtype=complex)
            for index, contents in attributes.items():
                if contents['p_a_ratio'] >= self.proportion:
                    partial_result += contents['signals']
            result.append(partial_result)
        return result
