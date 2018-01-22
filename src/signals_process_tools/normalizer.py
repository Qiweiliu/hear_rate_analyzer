from sklearn.preprocessing import scale


class Normalizer:
    def normalize(self, signals):
        return scale(signals)
