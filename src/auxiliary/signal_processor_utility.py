from auxiliary.io_utility import IOUtility


class SignalProcessorUtility(IOUtility):

    def __init__(self, data):
        super().__init__(data)
        self.data = data

    def read(self):
        """
        Incorporate all signals into a single list
        :return:
        """
        integrated_signals = []
        for antennas, content in self.data.items():
            for index, signals in content.items():
                integrated_signals.append(
                    signals
                )
        return integrated_signals

    def pack(self, filtered_signals):
        """
        Pack processed result with the formal dictionary by the feature of the ordered list
        :param filtered_signals:
        :return:
        """
        i = 0
        for antennas, content in self.data.items():
            for index, signals in content.items():
                self.data[antennas][index] = filtered_signals[i]
                i += 1
        return self.data
