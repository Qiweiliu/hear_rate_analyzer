import numpy as np


class FftGenerator:
    """
    Generate ffts
    .warn:: The result from numpy.fft.fft is complex
     and will be converted to real number
    """

    def generate(self, signals_sets, size):
        """
        Generate fft results
        :param size: The size of input signals
        :param signals_sets: A list of time series signals. e.g. [[], []]
        :return: Return a list of fft result. Attention, the results are real number
        """
        result = []
        for signals in signals_sets:
            result.append(np.absolute(
                np.fft.fft(a=signals,
                           n=size
                           )
            )
            )
        return result
