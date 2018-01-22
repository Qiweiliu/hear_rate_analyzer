import unittest
import numpy as np
from signal_source.arduino_signals import Arduino


class MockSocket:
    def __init__(self):
        self.count = 0
        self.mock_data = np.load('../test_assets/test_signal_arduino/mock_arduino_signal.npy')

    def readline(self):
        return self.mock_data[self.count]


class TestArduino(unittest.TestCase):

    def setUp(self):
        self.arduino = Arduino(window_length=1, socket=MockSocket())

    def test_get_sample_rate_a(self):
        """
        Test get sample rate. The sample rate is calculated from count divided by the window length
        :return:
        """
        self.arduino.get()
        self.assertEqual(self.arduino.get_sample_rate(), 1)

    def test_get_sample_rate_b(self):
        # TODO: To get mock data
        self.arduino.get()
        self.arduino.get()
        self.arduino.get()
        self.assertEqual(self.arduino.get_sample_rate(), 3)

    def test_get_sample_rate_when_new_window(self):
        arduino = Arduino(window_length=1, socket=MockSocket())
        arduino.get()
        self.assertEqual(1, arduino.get_sample_rate())
        arduino.get()
        self.assertEqual(1, arduino.get_sample_rate())
