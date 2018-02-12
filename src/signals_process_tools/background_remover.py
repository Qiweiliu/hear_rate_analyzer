import numpy as np

from auxiliary.static_filter_utility import StaticFilterUtility


class BackGroundRemover:
    def continuous_remove(self, raw_signals):
        """
        Remove background signals.
        Subtracting the current from the previous one.
        The shape of the matrix is not changed
            i.e.(number of sample, number of points every triggering)
            (340,4096)
        :param raw_signals:
        :return:
        """
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

    def initial_remove(self, raw_signals_sets):

        def remove(raw_signals):
            base_list = np.tile(raw_signals[0], ((len(raw_signals) - 1), 1))
            subtracted_signals = np.subtract(raw_signals[1:], base_list)
            return subtracted_signals

        static_filter_utility = StaticFilterUtility(raw_signals_sets)

        i = 0
        signals = static_filter_utility.read()
        for key in raw_signals_sets.keys():
            raw_signals_sets[key] = remove(signals[i])
            i += 1
        return raw_signals_sets
