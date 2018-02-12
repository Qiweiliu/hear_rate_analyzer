from auxiliary.data_manager import DataManager
from auxiliary.decoder import Decoder
from auxiliary.signal_visualizer import SignalVisualizer
import matplotlib.pyplot as plt
import seaborn as sns;
import numpy as np

from auxiliary.static_filter_utility import StaticFilterUtility
from signals_process_tools.bandpass_filter import BandPassFilter
from signals_process_tools.matrix_bandpass_filter import MatrixBandpassFilter
from sklearn import preprocessing
import matplotlib.pyplot as plt

from signals_process_tools.window_adder import WindowAdder

sns.set()

from signals_process_tools.background_remover import BackGroundRemover

data_manager = DataManager()
# 3_antennas_relax_no_breathe
data = data_manager.load(
    scenario='3_antennas_relax_no_breathe',
    path='../../data_collection')
sample_rate = data['sample_rate']
# read data
raw_signals = [data['walabot']]

# create decoder to decode signals from different antenna pairs
decoder = Decoder(raw_signals)
decoded_signals = decoder.decode()

# bandpass filter
bandpass_filter = BandPassFilter(
    lowcut=0.866,
    highcut=3.33,
    frequency=sample_rate,
    order=5
)

# remove background first
reader = StaticFilterUtility(decoded_signals)
background_remover = BackGroundRemover()
removed_background_matrix = background_remover.initial_remove(reader.read())[0]
# plt.plot(decoded_signals['1.0_4.0'].transpose()[50])
# plt.show()

# preprocess
# matrix_bandpass_filter = MatrixBandpassFilter(bandpass_filter=bandpass_filter)
# removed_matrix = matrix_bandpass_filter.filter_single_set(removed_background_matrix)

# ax = sns.heatmap(removed_matrix.transpose())
# plt.show()
#
# subtracked_signals = background_remover.continuous_remove(removed_matrix)


# for i in range(0,100):
#     plt.plot(removed_background_matrix[i])
#     plt.show()

#
#
# mix = removed_matrix.transpose()[195][100:]
# 162
mix = removed_background_matrix.transpose()[33]
# mix = bandpass_filter.filter([mix])[0]
# separate filter


# for i in range(1, 512):
#     mix += removed_matrix.transpose()[i]
#
#
#
# plt.plot(mix)
# plt.show()
#
signal_visualizer = SignalVisualizer()
plt.plot(mix)
plt.show()

fig = signal_visualizer.show_spectrum(
    np.absolute
        (
        np.fft.fft(mix, int(sample_rate / 0.01666666667))
    )
    ,
    sample_rate
)
plt.show(fig)
