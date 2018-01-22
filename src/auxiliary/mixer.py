from operator import add
import numpy as np


class Mixer:
    def mix(self, signal_sets):
        """
        Mixing signals.
        .warn:: The data type shall be responded to do addition operation
        :param signal_sets:
        :return:
        """
        result = np.array([0.0] * len(signal_sets[0]))
        for signals in signal_sets:
            result += signals

        # keep data format consistent by [ result ]
        return [result]
