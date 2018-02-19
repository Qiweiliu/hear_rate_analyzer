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
from main.batcher import Batcher
from main.signal_processor import SignalProcessor
from signals_process_tools.background_remover import BackGroundRemover
from signals_process_tools.bandpass_filter import BandPassFilter
from signals_process_tools.energy_ratio_analyzer import EnergyRatioAnalyzer
from signals_process_tools.fft_generator import FftGenerator
from signals_process_tools.matrix_bandpass_filter import MatrixBandpassFilter
from signals_process_tools.post_processor import SignalPostProcessor
from signals_process_tools.rate_analyzer import RateAnalyzer
from signals_process_tools.signal_preprocessor import SignalPreprocessor
from signals_process_tools.sliding_windows_maker import SlidingWindowsMaker
from signals_process_tools.static_filter import StdStaticFilter
import matplotlib.pyplot as plt
import numpy as np
from sklearn import preprocessing

# load data
data_manager = DataManager()
data = data_manager.load(
    scenario='3_antennas_office_half_distance_SENSOR_5_69_66',
    path='../../data_collection')

# read data
raw_signals = [data['walabot']]
sample_rate = data['sample_rate']
signal_visualizer = SignalVisualizer()


def run():
    # 0.866, 3.333, bandpass filter
    bandpass_filter = BandPassFilter(
        lowcut=0.866,
        highcut=3.333,
        frequency=sample_rate,
        order=5
    )

    # remove background signals
    background_remover = BackGroundRemover()

    # preprocess
    matrix_bandpass_filter = MatrixBandpassFilter(bandpass_filter=bandpass_filter)

    # create signal process components
    static_filter = StdStaticFilter(
        rank=10
    )

    # create signal_preprocessor
    signal_preprocessor = SignalPreprocessor(
        matrix_bandpass_filter=matrix_bandpass_filter,
        background_remover=background_remover,
        static_filter=static_filter
    )

    # -------------------------------------------------------------------------------------------------#

    fft_generator = FftGenerator()
    sliding_windows_maker = SlidingWindowsMaker(
        window_size=180,
        interval=18
    )

    energy_ration_sliding_windows_maker = SlidingWindowsMaker(
        window_size=60,
        interval=60
    )

    energy_ratio_analyzer = EnergyRatioAnalyzer(
        sliding_windows_maker=energy_ration_sliding_windows_maker,
        fft_generator=fft_generator,
        proportion=5
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

    # -------------------------------------------------------------------------------------------------#
    signal_postprocessor = SignalPostProcessor(
        mixer=Mixer()
    )
    # -------------------------------------------------------------------------------------------------#
    batcher = Batcher(
        signal_preprocessor=signal_preprocessor,
        signal_processor=signal_processor,
        signal_postprocessor=signal_postprocessor
    )
    # -------------------------------------------------------------------------------------------------#
    pprint.pprint(batcher.batcher_process(
        '../../data_collection'
    )
    )

def visualize():
    processed_result = np.load('../../temp/temp_processed_result.npy').item()
    print()

    # plt.show(
    #     signal_visualizer.show(
    #         processed_result=processed_result,
    #         antenna='1.0_3.0',
    #         distance='199',
    #         type='windows',
    #         number=0,
    #         sample_rate=sample_rate
    #     )
    # )


run()
# visualize()
