import numpy as np


class ArduinoFilter:

    def __init__(self):
        self.result = []
        self.values = []

    def reduce(self, values):
        """
        Calculate the mean of each sublist.
        ..warn:: The list format is: [[[1], [2], [3]], [1], [2], [3]]]
        The numpy mean will ignore brackets and calculates the mean of [[1], [2], [3]]
        :param values: The list from Arduino
        :return: Return list of the means of each sublist
        """
        for value in self.values:
            self.result.append(
                np.mean(value)
            )
        return self.result

    def filter_head(self, values, extend):
        # values = self.convert_list_format(values)
        for i in range(0, extend):
            for j in range(0, len(values[i])):
                values[i][j] = [None]
        return values

    def filter_zeros(self, values):
        """
        Filter the sublist which consists of zeros
        :param values:
        :return:
        """
        result = []

        for value in values:
            result.append()
