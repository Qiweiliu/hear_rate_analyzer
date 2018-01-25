import numpy as np


class EnergyRatioAnalyzer:
    """
    An energy ratio analyzer to divide a time series signals and divides it into different section.
    To calculate the maximum, average, and ratio.
    """

    def __init__(self, sliding_windows_maker, fft_generator):
        self.sliding_windows_maker = sliding_windows_maker
        self.fft_generator = fft_generator

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
        # TODO: The ffts size may have effects
        ffts = self.fft_generator.generate(windows, len(windows[0]))
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
                    ratio
            }
            i += 1
        return result
