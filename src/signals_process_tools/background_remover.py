import numpy as np


class BackGroundRemover:
    def remove(self, raw_signals):
        raw_signals = np.array(raw_signals)
        index = 1
        result = raw_signals[1] - raw_signals[0]
        while index + 1 < len(raw_signals):
            result = np.vstack((result,
                                raw_signals[index + 1]
                                -
                                raw_signals[index]
                                )
                               )
            index += 1
        return result
