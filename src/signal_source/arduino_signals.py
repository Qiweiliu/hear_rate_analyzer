import serial
import time
import numpy as np

from signal_source.source_base import SignalSourceBase


class Arduino(SignalSourceBase):
    """
    Get pulse amplitude from socket.
    """

    # TODO: To receive heart beats
    def __init__(self, socket, window_length=10):
        """
        Passing a socket for the initialization
        :param socket: A socket object specified with the port number and the buffer size. The default socket for the
        project is serial.Serial('COM3', 115200)
        :param window_length: The windows size which refers to the time duration
        """
        super().__init__()
        self.window_length = window_length
        self.ser = socket

    def get(self):
        """
        Get a single amplitude
        :return: Return a single amplitude
        :rtype: A list of signals. Return a list keep the data structure consistent and no need to write a new
        compatible program to read
        """
        self.count += 1
        output = self.ser.readline().decode("utf-8").rstrip()

        if output == '':
            return [0]
        else:
            return [output]
