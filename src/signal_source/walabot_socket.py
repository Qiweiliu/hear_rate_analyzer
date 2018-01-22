import socket
import time
from struct import unpack
from signal_source.source_base import SignalSourceBase


class WalabotSocket(SignalSourceBase):
    """
    Get a set of signal amplitudes by socket from C++ API
    """

    # TODO: Start and initialization

    def __init__(self, sample_number, type_of_size, window_length=10):
        """
        Initialization
        :param sample_number: The number of samples. i.e. 4096
        :param type_of_size: The size of single data. i.e. Double, 8 bytes
        :param window_length: the windows length measured by time
        """

        super().__init__()
        self.window_length = window_length
        self.type_of_size = type_of_size
        self.signals = []
        self.data = None
        self.size = sample_number * type_of_size
        self.initialize_socket()

    def initialize_socket(self):
        """
        Initialize socket that ensures the sample rate is not affected by the initialization of walabot
        """
        self.host = socket.gethostname()
        self.port = 27015  # The same port as used by the server
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.connect((self.host, self.port))
        self.s.send(b'initialize')
        return self.s.recv(self.size)

    def get(self):
        """
        One call to get() will trigger one pulse.
        :return: return a list of signal amplitudes indexed by distance.
        """
        self.count += 1
        self.signals = []
        self.s.send(b'test')
        self.data = self.s.recv(self.size)
        self._interpret()
        return self.signals

    def _interpret(self):
        base = 0
        while base <= self.size - self.type_of_size:
            self.signals.append(unpack('d', self.data[base: (base + self.type_of_size)])[0])
            base += self.type_of_size
