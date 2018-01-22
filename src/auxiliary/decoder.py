import numpy as np
from auxiliary.data_manager import DataManager


class Decoder:
    """
    Decode signals from different antennas
    The data is from walabot without any preprocess
    """

    def __init__(self, raw_data):
        self.raw_data = np.array(raw_data)[0]
        self.antenna_header = self.raw_data[0]

    def decode(self):
        antenna_pairs = self.read_antenna_pairs()
        result = {}

        # delete the antenna header and the hsplit
        self.raw_data = np.delete(self.raw_data, (0), axis=0)
        split_signals = np.hsplit(self.raw_data, len(antenna_pairs))

        i = 0
        for antenna_pair in antenna_pairs:
            result[str(antenna_pair[0]) + '_' + str(antenna_pair[1])] = split_signals[i]
            i += 1
        return result

    def read_antenna_pairs(self):
        """
        Read antenna pairs from raw data
        :return:
        """
        antenna_pairs = []
        for i in range(0, len(self.antenna_header), 2):
            if self.antenna_header[i] == 0.0:
                break
            antenna_pairs.append(
                (self.antenna_header[i],
                 self.antenna_header[i + 1]
                 )
            )
        return antenna_pairs


if __name__ == '__main__':
    data_manager = DataManager()
    data = data_manager.load(
        scenario='three_antennas_relax',
        path='../../data_collection')

    # read data
    raw_signals = [data['walabot']]
    decoder = Decoder(raw_signals)
    decoded = decoder.decode()
    print('test')
