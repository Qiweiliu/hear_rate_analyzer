from auxiliary.io_utility import IOUtility
import numpy as np


class OverlyReader(IOUtility):

    def __init__(self, data=None):
        """
        Initialization of the data.
        ..warn:: The self.data shall be initialized before calling any of the below functions
        :param data:
        """
        super().__init__(data)
        self.data = data

    def pack(self, filtered_signals):
        keys = self.data.keys()
        result = {}
        for key, details in zip(keys, filtered_signals):
            result[str(key)] = details

        return result

    def read(self):
        result = []
        for antenna_index, content in self.data.items():
            signal_sum = np.array([0] * self._get_window_length(), dtype=float)
            for distance_index, signals in content.items():
                signal_sum += signals
                result.append(signal_sum)
        return result

    def _get_window_length(self):
        """
        Get the length of signals. The format is fixed.
        :return:
        """
        return list(list(self.data.values())[0].values())[0].size
