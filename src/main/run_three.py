from auxiliary.data_manager import DataManager
from auxiliary.decoder import Decoder
from auxiliary.static_filter_utility import StaticFilterUtility
from signals_process_tools.background_remover import BackGroundRemover
from signals_process_tools.bandpass_filter import BandPassFilter
from signals_process_tools.static_filter import StdStaticFilter
import numpy as np
import matplotlib.pyplot as plt


def get(raw_signal, axis):
    """
    Only handle a set of signals in raw signals, e.g. raw_signals[0] = [[1,2],[3,4]]
    :return:
    """
    raw_signal = np.array(raw_signal)
    std = np.std(raw_signal, axis=axis)
    return std


def run():
    # load data
    data_manager = DataManager()
    # 3_antennas_relax_no_breathe
    data = data_manager.load(
        scenario='3_antennas_relax_no_breathe',
        path='../../data_collection')

    # read data
    raw_signals = [data['walabot']]
    sample_rate = data['sample_rate']

    # create decoder to decode signals from different antenna pairs
    decoder = Decoder(raw_signals)
    decoded = decoder.decode()
    test_signals = decoded['1.0_4.0']

    # filter unwanted signals out of the target frequency range
    static_filter_utility = StaticFilterUtility(decoded)
    bandpass_filter = BandPassFilter(
        lowcut=0.866,
        highcut=3.333,
        frequency=sample_rate,
        order=5
    )

    # read signals from different antennas into a list
    decoded_raw_signals = static_filter_utility.read()

    # remove background signals from signals of every antennas
    background_remover = BackGroundRemover()
    removed_signals = []
    for i in range(0, len(decoded_raw_signals)):
        removed_signals.append(
            background_remover.initial_remove(
                decoded_raw_signals[i]
            )
        )

    i = 0
    for key in decoded.keys():
        decoded[key] = np.array(bandpass_filter.filter(removed_signals[i].transpose())).transpose()
        i += 1

    filtered_std = get(decoded['1.0_4.0'], 0)

    raw_std = get(test_signals, 0)

    plt.plot(raw_std, 'r')

    plt.plot(filtered_std, 'g')
    plt.show()
    print()


run()
