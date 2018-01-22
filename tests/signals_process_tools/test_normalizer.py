import unittest

import numpy as np

from signals_process_tools.normalizer import Normalizer


class TestNormalizer(unittest.TestCase):
    def setUp(self):
        self.signals = np.load('../test_assets/test_normalizer/time_series_heart_rate_0.npy')[100:]

    def test_normalize_signals(self):
        """
            No assertion here but why? what is the purpose of the test? It is likely to be a learning
        test instead of a unit test. It didn't achieve the functionality of a unit test.
        That is, make things easy to change and discover bugs immediately

        how to organize such kinds of tests? The learning tests?
            The learning test is also important during the development. Organize learning test rather than
            giving them up
            The naming convention:
                keep consistent and standard is enough for a personal project
            move it to a separate test instance
        """
        normalizer = Normalizer()
        normalized_signals = normalizer.normalize(self.signals)
        print(normalized_signals)
