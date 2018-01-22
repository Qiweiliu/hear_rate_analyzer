class SlidingWindowsMaker:
    """
    Return an list of windows by sliding
    """

    def __init__(self, window_size, interval):
        self.interval = interval
        self.window_size = window_size

    def get(self, signals):
        """
        Get all signals by sliding windows. It will make use of all possible windows though the inter-
        val is odd or even
        :param signals: a list of signals
        :return: an list of windows
        """
        windows = []
        start = 0
        end = self.window_size
        max_window_number = int((len(signals) - self.window_size) / self.interval + 1)
        for i in range(0, max_window_number):
            windows.append(
                signals[start
                        :
                        end]
            )
            start += self.interval
            end += self.interval
        return windows
