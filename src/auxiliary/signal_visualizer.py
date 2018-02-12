import matplotlib.pyplot as plt
import numpy as np


class SignalVisualizer:
    """
    Design for visualizing the
    """

    def show(self, processed_result, antenna, distance, type, number, sample_rate):
        signals = processed_result[str(antenna)][str(distance)][str(type)][number]
        if type == 'ffts':
            return self.show_spectrum(
                signals,
                sample_rate
            )

        fig = plt.figure()
        ax = fig.gca(projection='3d')

        # np.save('noises_ffts_sample',processed_result['1.0_4.0']['374']['ffts'][0])

        ax.plot(np.arange(0, len(signals)), [number] * len(signals), signals)
        return fig

    def show_spectrum(self, ffts, sample_rate):
        fig = plt.figure()
        ax = fig.add_subplot(111)
        ax.plot(np.absolute(
            np.fft.fftfreq(
                len(ffts),
                1 / sample_rate
            ) * 60
        ),
            ffts
        )
        return fig

    def show_two_dimension(self, signals):
        fig = plt.figure()
        ax = fig.add_subplot(111)
        ax.plot(np.absolute(signals))
        return ax

    def show_3d(self, signals):
        fig = plt.figure()
        ax = fig.gca(projection='3d')

        ax.plot(np.arange(0, len(signals)), [0] * len(signals), signals)
        return fig
