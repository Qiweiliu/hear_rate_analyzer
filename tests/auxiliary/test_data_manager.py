import unittest

from auxiliary.data_manager import DataManager


class TestDataManager(unittest.TestCase):
    """
    Test data structure and mongdb connection
    .. warning:: The test requires mongdb to keep open
    """

    def setUp(self):
        self.data_manager = DataManager()

    def test_save_data(self):
        # delete test collection first and then add a set of data to verify

        mock_walabot_signals = [[1, 2]]
        mock_arduino_signals = [[6]]
        mock_sample_rates = 1
        self.data_manager.save(walabot_signals=mock_walabot_signals,
                               arduino_signals=mock_arduino_signals,
                               sample_rate=mock_sample_rates,
                               scenario='test',
                               path='../test_assets/test_data_manager')

        data = self.data_manager.load(scenario='test',
                                      path='../test_assets/test_data_manager')
        self.assertEqual([[1, 2]], data['walabot'])
        self.assertEqual([[6]], data['arduino'])
        self.assertEqual(1, data['sample_rate'])
