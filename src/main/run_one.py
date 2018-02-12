import pprint
from mpl_toolkits.mplot3d import Axes3D
from auxiliary.data_manager import DataManager
from auxiliary.decoder import Decoder
from auxiliary.mixer import Mixer
from auxiliary.overly_reader import OverlyReader
from auxiliary.selector import Selector
from auxiliary.signal_processor_utility import SignalProcessorUtility
from auxiliary.signal_visualizer import SignalVisualizer
from auxiliary.static_filter_utility import StaticFilterUtility
from main.signal_processor import SignalProcessor
from signals_process_tools.background_remover import BackGroundRemover
from signals_process_tools.bandpass_filter import BandPassFilter
from signals_process_tools.energy_ratio_analyzer import EnergyRatioAnalyzer
from signals_process_tools.fft_generator import FftGenerator
from signals_process_tools.matrix_bandpass_filter import MatrixBandpassFilter
from signals_process_tools.rate_analyzer import RateAnalyzer
from signals_process_tools.sliding_windows_maker import SlidingWindowsMaker
from signals_process_tools.static_filter import StdStaticFilter
import matplotlib.pyplot as plt
import numpy as np

# load data
data_manager = DataManager()
data = data_manager.load(
    scenario='3_antennas_office_0_distance_postExercise_noBreathe_0',
    path='../../data_collection')

# read data
raw_signals = [data['walabot']]
sample_rate = data['sample_rate']


def run():
    # create decoder to decode signals from different antenna pairs
    decoder = Decoder(raw_signals)
    decoded = decoder.decode()

    # 0.866, 3.333
    # bandpass filter
    bandpass_filter = BandPassFilter(
        lowcut=0.866,
        highcut=3.333,
        frequency=sample_rate,
        order=5
    )

    # remove background signals
    background_remover = BackGroundRemover()
    removed_background_matrix = background_remover.initial_remove(decoded)

    # preprocess
    matrix_bandpass_filter = MatrixBandpassFilter(bandpass_filter=bandpass_filter)
    decoded = matrix_bandpass_filter.filter(removed_background_matrix)

    # create signal process components
    static_filter = StdStaticFilter()
    filtered_dynamic_signals = static_filter.filter(decoded, 50)

    fft_generator = FftGenerator()
    sliding_windows_maker = SlidingWindowsMaker(
        window_size=600,
        interval=600
    )

    energy_ration_sliding_windows_maker = SlidingWindowsMaker(
        window_size=200,
        interval=200
    )

    energy_ratio_analyzer = EnergyRatioAnalyzer(
        sliding_windows_maker=energy_ration_sliding_windows_maker,
        fft_generator=fft_generator,
        proportion=10
    )

    signal_processor_utility = SignalProcessorUtility()
    # signal_processor_utility = OverlyReader()

    # set up signal processor
    signal_processor = SignalProcessor(
        sample_rate=sample_rate,
        fft_generator=energy_ratio_analyzer,
        sliding_windows_maker=sliding_windows_maker,
        bandpass_filter=bandpass_filter,
        signal_processor_utility=signal_processor_utility
    )

    processed_result = signal_processor.process(filtered_dynamic_signals)
    np.save('../../temp/temp_processed_result', processed_result)
    # define selector, mix signals, and calculate heart rates
    mixer = Mixer()
    selector = Selector(processed_result)
    number_of_heart_rates = len((list(list(processed_result.values())[0].values())[0])['windows'])

    heart_rates = []
    for i in range(0, number_of_heart_rates):
        selected_ffts = selector.select_all_ffts(number=i)

        # select antennas
        # selected_ffts = selector.select_antenna_pairs(['1.0_4.0'], i)

        # mix signals

        mixed_result = mixer.mix(selected_ffts)

        # get heart rate result
        rate_analyzer = RateAnalyzer(mixed_result, sample_rate)
        heart_rates.append(rate_analyzer.get())

    print('The heart rates are:', heart_rates)


def visualize():
    processed_result = np.load('../../temp/temp_processed_result.npy').item()
    print()

    signal_visualizer = SignalVisualizer()
    plt.show(
        signal_visualizer.show(
            processed_result=processed_result,
            antenna='1.0_4.0',
            distance='34',
            type='ffts',
            number=0,
            sample_rate=sample_rate
        )
    )


run()
visualize()
