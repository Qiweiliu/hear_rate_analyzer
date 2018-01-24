import matplotlib.pyplot as plt
import numpy as np


class SignalVisualizer:
    """
    Design for visualizing the
    """

    def __init__(self, processed_result):
        self.processed_result = processed_result
        pass

    def show(self, antenna, distance, type, number):
        fig = plt.figure()
        ax = fig.gca(projection='3d')
        signals = self.processed_result[str(antenna)][str(distance)][str(type)][number]
        ax.plot(np.arange(0, len(signals)), [number] * len(signals), signals)
        # plt.show(fig)
        return fig

    def show_spectrum(self, ffts, sample_rate):
        fig = plt.figure()
        ax = fig.add_subplot(111)
        ax.plot(np.absolute(
            np.fft.fftfreq(
                len(ffts),
                1 / sample_rate
            ) * 60),
            ffts
        )
        return fig
