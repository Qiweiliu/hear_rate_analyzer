import unittest
from scipy import signal
import numpy as np
import matplotlib.pyplot as plt

from signals_process_tools.window_adder import WindowAdder


class TestWindowsAdder(unittest.TestCase):

    def setUp(self):
        sampling_rate = 8000
        t = np.arange(0, 1.0, 1.0 / sampling_rate)
        self.signal_list = np.sin(2 * np.pi * 50 * t)[:512]
        self.signal_list = [self.signal_list, self.signal_list]
        self.windows_adder = WindowAdder()

    def test_add(self):
        added_window = signal.hamming(512) * self.signal_list[0]
        self.assertEqual(added_window[0],
                         self.windows_adder.add(
                             self.signal_list
                         )[0][0]
                         )
        self.assertEqual(added_window[0],
                         self.windows_adder.add(
                             self.signal_list
                         )[1][0]
                         )
