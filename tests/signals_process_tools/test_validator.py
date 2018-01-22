import unittest

from main.validator import Validator


class TestValidator(unittest.TestCase):
    def setUp(self):
        self.validator = Validator()
        self.mock_walabot = [1, 2, 3, 4, 5, 6, 7]
        self.mock_arduino = [7, 6, 5, 9, 3, 2, 1]
        pass

    def test_validate_by_median(self):
        # TODO: Add the weight algorithm
        self.assertAlmostEqual(
            0.77777799999999997,
            self.validator.validate_by_median(
                self.mock_walabot,
                self.mock_arduino
            )
        )

    def test_validate_windows(self):
        # TODO: How to handle the difference of the windows number?

        pass
