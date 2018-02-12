import pprint
import matplotlib.pyplot as plt
from auxiliary.data_manager import DataManager
from auxiliary.decoder import Decoder
from auxiliary.overly_reader import OverlyReader
from auxiliary.signal_processor_utility import SignalProcessorUtility
from auxiliary.static_filter_utility import StaticFilterUtility
from main.signal_processor import SignalProcessor
from signals_process_tools.bandpass_filter import BandPassFilter
from signals_process_tools.energy_ratio_analyzer import EnergyRatioAnalyzer
from signals_process_tools.fft_generator import FftGenerator
from signals_process_tools.matrix_bandpass_filter import MatrixBandpassFilter
from signals_process_tools.sliding_windows_maker import SlidingWindowsMaker
from signals_process_tools.static_filter import StdStaticFilter


def run():
    # load data
    data_manager = DataManager()
    data = data_manager.load(
        scenario='3_antennas_relax_0blocks_Narrow_lchest__exercise_0_86_90',
        path='../../data_collection')

    # read data
    raw_signals = [data['walabot']]
    sample_rate = data['sample_rate']

    # create decoder to decode signals from different antenna pairs
    decoder = Decoder(raw_signals)
    decoded = decoder.decode()

    # new bandpass filter
    # 0.866, 3.333
    bandpass_filter = BandPassFilter(
        lowcut=0.866,
        highcut=3.333,
        frequency=sample_rate,
        order=5
    )

    # preprocess
    matrix_bandpass_filter = MatrixBandpassFilter(bandpass_filter=bandpass_filter)
    decoded = matrix_bandpass_filter.filter(decoded)

    # create signal process components
    static_filter = StdStaticFilter()
    filtered_dynamic_signals = static_filter.filter(decoded, 1)

    fft_generator = FftGenerator()

    signal_processor_utility = SignalProcessorUtility()

    sliding_windows_maker = SlidingWindowsMaker(
        window_size=600,
        interval=600
    )

    # set up signal processor
    signal_processor = SignalProcessor(
        sample_rate=sample_rate,
        fft_generator=fft_generator,
        sliding_windows_maker=sliding_windows_maker,
        bandpass_filter=bandpass_filter,
        signal_processor_utility=signal_processor_utility
    )

    processed_result = signal_processor.process(filtered_dynamic_signals)
    # visualize
    print()
    # plt.plot(processed_result['1.0_4.0']['windows'][0])
    # plt.show()


run()
