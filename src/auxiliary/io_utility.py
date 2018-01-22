from abc import ABC, abstractmethod


class IOUtility:
    @abstractmethod
    def __init__(self, data):
        pass

    @abstractmethod
    def read(self):
        pass

    @abstractmethod
    def pack(self, filtered_signals):
        pass
