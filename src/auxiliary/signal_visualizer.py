import matplotlib.pyplot as plt


class SignalVisualizer:
    def __init__(self):
        pass

    def show_histogram(self, list):
        plt.hist(list)
        plt.show()


if __name__ == '__main__':
    signal_visualizer = SignalVisualizer()
    signal_visualizer.show_histogram([1, 2, 3, 4, 5, 6, 7, 7, 8, 6, 4, 2, 2, 4, 324, 3, 4])
