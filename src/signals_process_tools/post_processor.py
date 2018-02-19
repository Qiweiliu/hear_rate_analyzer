from auxiliary.selector import Selector
import numpy as np
from sklearn import preprocessing

from signals_process_tools.rate_analyzer import RateAnalyzer


class SignalPostProcessor:
    def __init__(self, mixer):
        self.mixer = mixer

    def post_process(self, processed_result, sample_rate):
        heart_rates = []
        selector = Selector(processed_result)
        number_of_heart_rates = len((list(list(processed_result.values())[0].values())[0])['windows'])
        for i in range(0, number_of_heart_rates):
            selected_ffts = np.absolute(selector.select_all_ffts(number=i))

            selected_ffts = preprocessing.normalize(selected_ffts)
            # select antennas
            # selected_ffts = selector.select_antenna_pairs(['1.0_4.0'], i)

            # mix signals
            mixed_result = self.mixer.mix(selected_ffts)
            # plt.show(signal_visualizer.show_spectrum(
            #     mixed_result[0], sample_rate
            # ))

            # get heart rate result
            rate_analyzer = RateAnalyzer(mixed_result, sample_rate)
            heart_rates.append(rate_analyzer.get()[0])
        heart_rates = np.around(heart_rates)
        return heart_rates
