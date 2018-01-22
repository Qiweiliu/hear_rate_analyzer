import numpy as np


class Validator:
    def validate_by_median(self, walabot, arduino):
        walabot_median = np.median(walabot)
        arduino_median = np.median(arduino)
        return self.get_percentage_similarity(walabot_median, arduino_median)

    def get_percentage_similarity(self, walabot_median, arduino_median):
        similarity = 1 - abs(walabot_median - arduino_median) \
                     / ((walabot_median + arduino_median) / 2)
        similarity = np.around(similarity, decimals=6)
        return similarity
