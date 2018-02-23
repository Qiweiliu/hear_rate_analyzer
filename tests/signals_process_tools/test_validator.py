import unittest

from main.validator import Validator


class TestValidator(unittest.TestCase):
    def setUp(self):
        self.validator = Validator()
        self.mock_oximeter = {
            '1': [1, 2, 3],
            '2': [4, 5, 6]
        }
        self.mock_result = {
            '1': [1, 1, 1],
            '2': [4, 4, 4]
        }
        pass

    def test_validate(self):
        result = self.validator.validate(
            result=self.mock_result,
            ground_truth=self.mock_oximeter
        )
        self.assertAlmostEqual(
            result['1'],
            0.66,
            1
        )

        self.assertAlmostEqual(
            result['2'],
            0.22,
            1
        )
