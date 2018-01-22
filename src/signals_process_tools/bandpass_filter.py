from scipy.signal import butter, lfilter


class BandPassFilter():
    def __init__(self, lowcut, highcut, frequency, order):
        self.lowcut = lowcut
        self.highcut = highcut
        self.frequency = frequency
        self.order = order

    def filter(self, signals):
        result = []
        b, a = self._set_butter_bandpass()
        for signal in signals:
            result.append(lfilter(b, a, signal))
        return result

    def _set_butter_bandpass(self):
        nyq = 0.5 * self.frequency
        low = self.lowcut / nyq
        high = self.highcut / nyq
        b, a = butter(self.order, (low, high), btype='bandpass')
        return b, a
