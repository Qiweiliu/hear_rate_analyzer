import time
import numpy as np
from multiprocessing import Process

from signal_source.source_base import SignalSourceBase


class SignalGetter(Process):
    """
    A signal getter reads signal from a signal source. It inherits from Process class
    which enables multiprocess
    """

    def __init__(self, total_duration_time=10):
        super().__init__()
        self.signal_source = SignalSourceBase()
        self.total_duration_time = total_duration_time
        self.result = []

    def start(self):
        return self.get_full_windows()

    def set_signal_source(self, signal_source):
        self.signal_source = signal_source

    def get_signal(self):
        return self.signal_source.get()

    def get_full_windows(self):
        """
        Get signals of a windows length.
        :return: (list of list of signals, the sample rate of those list )
        """
        signal_sets = []
        while self.signal_source.if_continue():
            signal_sets.append(self.signal_source.get())
        return signal_sets, self.signal_source.get_sample_rate()

    def if_continue(self):
        if time.time() - self.start < self.total_duration_time:
            return True
        else:
            return False

    def save(self, file_path):
        np.save(file_path, np.array(self.result))
