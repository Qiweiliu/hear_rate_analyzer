from auxiliary.io_utility import IOUtility


class StaticFilterUtility(IOUtility):
    def __init__(self, data):
        super().__init__(data)
        self.data = data
        self.signal_sets = []
        self.antennas = list(self.data.keys())

    def pack(self, filtered_signals):
        """
        Shall be called after read() called
        :return:
        """
        result = {}
        antenna_index = 0
        for signals_pairs in filtered_signals:
            result[self.antennas[antenna_index]] = {}
            for index, signals in signals_pairs:
                result[self.antennas[antenna_index]][str(index)] = signals
            antenna_index += 1

        return result

    def read(self):
        # clear before add
        self.signal_sets = []
        for antenna_pair, signals in self.data.items():
            self.signal_sets.append(signals)
        return self.signal_sets
