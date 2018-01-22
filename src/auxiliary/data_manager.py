import numpy as np


class DataManager:
    """
    To load data
    ..warn:: pay attention to the data format of
    arduino that needs to be extract
    """

    def __init__(self):
        pass

    def save(self, walabot_signals,
             arduino_signals, sample_rate, scenario, path='../data_collection'):
        data = {'walabot': walabot_signals,
                'arduino': arduino_signals,
                'sample_rate': sample_rate}

        np.save(path + '/' + scenario, data)

    def load(self, scenario, path='../data_collection'):
        return np.load(path + '/' + scenario + '.npy').item()
