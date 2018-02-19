import numpy as np

from auxiliary.static_filter_utility import StaticFilterUtility


class StdStaticFilter:
    """
    Eliminate static signal by the standard deviation
    """

    def __init__(self, rank):
        self.rank = rank

    def filter(self, raw_dictionary):
        """
        :param raw_dictionary: A set of raw signals returned by Walabot.The format is [[[],[]], [[],[]]]
        The index of the list represents the distance
        :param rank: The expected number of signals
        :return: return n candidate filtered signals and their corresponding indices that are distances.
        e.g. [(int index,float[] filtered_signals )]
        """

        # TODO: The return value has a deep nested structure
        def get(raw_signal):
            """
            Only handle a set of signals in raw signals, e.g. raw_signals[0] = [[1,2],[3,4]]
            :return:
            """
            raw_signal = np.array(raw_signal)
            std = np.std(raw_signal, axis=0)

            # only sort indices
            n_largest_index = np.argsort(std)[-self.rank:]
            n_largest_contiguous_signals = raw_signal[:, n_largest_index]

            i = 0
            max_signals = []
            for index in n_largest_index:
                max_signals.append((index, n_largest_contiguous_signals[:, i]))
                i += 1
            return max_signals

        # define filtered result
        filtered_signals = []

        # define reader
        static_filter_utility = StaticFilterUtility(raw_dictionary)
        raw_signals = static_filter_utility.read()
        for raw_signal in raw_signals:
            filtered_signals.append(get(raw_signal))
        return static_filter_utility.pack(filtered_signals)
