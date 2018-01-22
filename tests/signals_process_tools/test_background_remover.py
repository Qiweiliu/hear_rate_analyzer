import unittest
import numpy as np

from signals_process_tools.background_remover import BackGroundRemover


class TestBackgroundRemover(unittest.TestCase):
    def setUp(self):
        self.mock_signals = np.array([
            [1, 2, 3, 4, 5, 6],
            [6, 5, 4, 3, 2, 1],
            [1, 1, 1, 1, 1, 1]
        ])
        self.background_remover = BackGroundRemover()

    def test_remove(self):
        """
        The index subscription follow the rules of numpy
        :return:
        """
        result = self.background_remover.remove(self.mock_signals)
        # print(result)
        self.assertEqual(len(result), len(self.mock_signals) - 1)
        self.assertEqual(5, result[0][0])
        self.assertEqual(0, result[1][5])
