from auxiliary.decoder import Decoder


class SignalPreprocessor:
    def __init__(self, matrix_bandpass_filter, background_remover, static_filter):
        self.static_filter = static_filter
        self.background_remover = background_remover
        self.matrix_bandpass_filter = matrix_bandpass_filter

    def preprocess(self, raw_signals):
        # create decoder to decode signals from different antenna pairs
        decoder = Decoder(raw_signals)
        decoded = decoder.decode()

        # remove background signals
        decoded = self.background_remover.initial_remove(decoded)

        decoded = self.matrix_bandpass_filter.filter(decoded)

        # create signal process components
        filtered_dynamic_signals = self.static_filter.filter(decoded)
        return filtered_dynamic_signals
