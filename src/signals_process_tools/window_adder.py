from scipy import signal


class WindowAdder:

    def add(self, signal_list):
        """
        Add hamming windows.
        The signal.hamming(sym = false), sym is set to false for the spectral analysis
        :param signal_list: A list of time series signals
        :return: A list window-added signals
        """
        result = []
        for signals in signal_list:
            result.append(
                signals * signal.blackmanharris(
                    len(signals),
                    sym=False
                )
            )
        return result
