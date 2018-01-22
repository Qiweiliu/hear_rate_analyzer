import unittest
import numpy as np

from signal_source.source_base import SignalSourceBase
from signals_process_tools.signal_getter import SignalGetter


class MockSignalSource(SignalSourceBase):
    def get_sample_rate(self):
        """
        Return a sample rate
        :return: Return a fixed sample rate
        """
        return 1

    def __init__(self, window_length=5):
        self.count = [-1]
        self.max = window_length

    def get(self):
        self.count[0] += 1
        temp = [self.count[0]]
        return temp

    def if_continue(self):
        if self.count[0] < self.max:
            return True
        else:
            return False


class TestSignalGetter(unittest.TestCase):
    def setUp(self):
        self.signal_getter = SignalGetter()
        self.mock_signal = MockSignalSource()

    def test_get_signal(self):
        """
        Test get signal. Get a single signal.
        """

        self.signal_getter.set_signal_source(MockSignalSource())
        self.assertEqual(self.signal_getter.get_signal(), [0])
        self.assertEqual(self.signal_getter.get_signal(), [1])
        self.assertEqual(self.signal_getter.get_signal(), [2])

    def test_get_full_windows(self):
        signal_getter = SignalGetter()
        signal_getter.set_signal_source(MockSignalSource())
        self.assertEqual(signal_getter.get_full_windows()[0], [[0], [1], [2], [3], [4], [5]])

    def test_set_signal_source(self):
        self.signal_getter.set_signal_source(self.mock_signal)
        mock_signal_source = self.signal_getter.signal_source
        self.assertEqual(mock_signal_source.get(), [0])
        self.assertEqual(mock_signal_source.get(), [1])
        self.assertEqual(mock_signal_source.get(), [2])
        self.assertEqual(mock_signal_source.get(), [3])
        self.assertEqual(mock_signal_source.get(), [4])

    def test_save(self):
        signal_getter = SignalGetter(total_duration_time=0.001)
        self.signal_getter.result = np.array([1, 2, 3])
        self.signal_getter.save('../test_assets/test_signal_getter/test')
        self.assertEqual(np.load('../test_assets/test_signal_getter/test.npy')[0], 1)
        self.assertEqual(np.load('../test_assets/test_signal_getter/test.npy')[1], 2)
        self.assertEqual(np.load('../test_assets/test_signal_getter/test.npy')[2], 3)

    def test_mock_signal(self):
        mock_signal = MockSignalSource()
        self.assertEqual(mock_signal.get(), [0])
        self.assertEqual(mock_signal.get(), [1])
        self.assertEqual(mock_signal.get(), [2])
        self.assertEqual(mock_signal.get(), [3])
        self.assertEqual(mock_signal.get(), [4])

    def test_mock_signal_if_continue(self):
        mock_signal_source = MockSignalSource()
        for i in range(0, 7):
            mock_signal_source.get()

        self.assertFalse(mock_signal_source.if_continue())
