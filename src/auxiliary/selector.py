import numpy as np


class Selector:
    """
    Select expected data from the result dictionary
    """

    def __init__(self, data):
        self.data = data

    def select_all_ffts(self, number):
        """
        Select signals from all distance and all antennas pairs
        :param number: The index of the windows that are divided by sliding windows maker
        :return: an nested list including all expect ffts results. e.g. [[], [], [], []]
        """
        result = []
        for antennas, content in self.data.items():
            for index, intermediate_result in content.items():
                result.append(intermediate_result['ffts'][number])
        return result

    def select_antenna_pairs(self, antenna_pairs, number):
        result = []
        for antennas, content in self.data.items():
            if antennas in antenna_pairs:
                for index, intermediate_result in content.items():
                    result.append(intermediate_result['ffts'][number])
        return result
