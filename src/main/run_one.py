import pprint

import numpy as np

from auxiliary.data_manager import DataManager
from auxiliary.mixer import Mixer
from auxiliary.signal_processor_utility import SignalProcessorUtility
from auxiliary.signal_visualizer import SignalVisualizer
from main.batcher import Batcher
from main.signal_processor import SignalProcessor
from signals_process_tools.background_remover import BackGroundRemover
from signals_process_tools.bandpass_filter import BandPassFilter
from signals_process_tools.energy_ratio_analyzer import EnergyRatioAnalyzer
from signals_process_tools.fft_generator import FftGenerator
from signals_process_tools.matrix_bandpass_filter import MatrixBandpassFilter
from signals_process_tools.post_processor import SignalPostProcessor
from signals_process_tools.signal_preprocessor import SignalPreprocessor
from signals_process_tools.sliding_windows_maker import SlidingWindowsMaker
from signals_process_tools.static_filter import StdStaticFilter


def run():
    # -------------------------------Initialize Preprocessor------------------------------#
    # 0.866, 3.333, bandpass filter
    matrix_bandpass_filter_utility = BandPassFilter(
        lowcut=0.866,
        highcut=3.333,
        order=5
    )

    # remove background signals
    background_remover = BackGroundRemover()

    # preprocess
    matrix_bandpass_filter = MatrixBandpassFilter(bandpass_filter=matrix_bandpass_filter_utility)

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

    # -------------------------------Initialize Processor------------------------------#

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

    # define bandpass filter for signal processor
    processor_bandpass_filter = BandPassFilter(
        lowcut=0.866,
        highcut=3.333,
        order=5
    )

    # set up signal processor
    signal_processor = SignalProcessor(
        fft_generator=energy_ratio_analyzer,
        sliding_windows_maker=sliding_windows_maker,
        bandpass_filter=processor_bandpass_filter,
        signal_processor_utility=signal_processor_utility
    )

    # -------------------------------Initialize Postprocessor------------------------------#
    signal_postprocessor = SignalPostProcessor(
        mixer=Mixer()
    )
    # -------------------------------Initialize Batcher------------------------------#
    batcher = Batcher(
        signal_preprocessor=signal_preprocessor,
        signal_processor=signal_processor,
        signal_postprocessor=signal_postprocessor
    )
    # -------------------------------Run------------------------------#
    pprint.pprint(batcher.batcher_process(
        '../../data_collection/static_scenario'
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
