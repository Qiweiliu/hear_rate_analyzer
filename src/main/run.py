from auxiliary.data_manager import DataManager
from auxiliary.decoder import Decoder
from auxiliary.mixer import Mixer
from auxiliary.selector import Selector
from main.signal_processor import SignalProcessor
from signals_process_tools.bandpass_filter import BandPassFilter
from signals_process_tools.fft_generator import FftGenerator
from signals_process_tools.rate_analyzer import RateAnalyzer
from signals_process_tools.sliding_windows_maker import SlidingWindowsMaker
from signals_process_tools.static_filter import StdStaticFilter
import matplotlib.pyplot as plt
import numpy as np

# load data
data_manager = DataManager()
data = data_manager.load(
    scenario='3_antennas_exercise_0_98_100',
    path='../../data_collection')

# read data
raw_signals = [data['walabot']]
sample_rate = data['sample_rate']
arduino_heart_rates = data['arduino']
# arduino_heart_rates = np.array(
#     arduino_heart_rates,
#     dtype=int
# )

# create decoder to decode signals from different antenna pairs
decoder = Decoder(raw_signals)
decoded = decoder.decode()

# create signal process components
static_filter = StdStaticFilter()
filtered_dynamic_signals = static_filter.filter(decoded, 10)
fft_generator = FftGenerator()
sliding_windows_maker = SlidingWindowsMaker(
    window_size=330,
    interval=330
)

# 0.866, 3.333
bandpass_filter = BandPassFilter(
    lowcut=0.866,
    highcut=3.333,
    frequency=sample_rate,
    order=5
)

# set up signal processor
signal_processor = SignalProcessor(
    sample_rate, fft_generator, sliding_windows_maker,
    bandpass_filter
)
processed_result = signal_processor.process(filtered_dynamic_signals)

# check content
# Todo: write a visualizer to visualize
# plot 3d
fig = plt.figure()
ax = fig.gca(projection='3d')
signals = processed_result['1.0_7.0']['441']['windows'][0][0:100]
ax.plot(np.arange(0, len(signals)), [441] * len(signals), signals)
plt.show()

# define selector
selector = Selector(processed_result)
selected_ffts = selector.select_all_ffts(number=0)

# select antennas
# selected_ffts = selector.select_antenna_pairs(['1.0_7.0'], 0)

# mix signals
mixer = Mixer()
mixed_result = mixer.mix(selected_ffts)

# get heart rate result
rate_analyzer = RateAnalyzer(mixed_result, sample_rate)

# plot result
plt.plot(np.absolute(
    np.fft.fftfreq(
        len(mixed_result[0]),
        1 / sample_rate) * 60),
    mixed_result[0])
plt.show()
print(rate_analyzer.get())

# heart_rate_medians = []
# indices = []

# temporal experiment
# mix_signals = [0]*len(outputs[0][1])
# print(len(mix_signals))
# for index,signals in outputs:
#     mix_signals = list(map(add, mix_signals, signals))
# result = np.median(signal_processor.process(mix_signals))


# # handle every set of data
# mix_signals = [0] * int(
#     np.around(
#         sample_rate / 0.01666666667)
# )
# for index, signals in outputs:
#     print('The index is: ', index)
#     # signals = signal.savgol_filter(signals, len(signals), 10)
#     result_dictionary = signal_processor.process(signals)
#     # print_result(result_dictionary,0)
#     mix_signals = list(map(add, mix_signals, result_dictionary['ffts'][0]))
#
# print(len(mix_signals))
# plt.plot(np.absolute(
#     np.fft.fftfreq(
#         len(mix_signals),
#         1 / sample_rate) * 60),
#     mix_signals)
# plt.show()
