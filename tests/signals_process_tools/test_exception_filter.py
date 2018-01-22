import unittest

from signals_process_tools.exception_filter import ExceptionFilter


class TestExceptionFilter(unittest.TestCase):
    # TODO: The way to filter the exception has problems!!!
    def test_filter_exception_one(self):
        """
        try to filter the data whose variation is above 10%
        """
        exception_filter = ExceptionFilter(0.12)
        heart_rates = [60, 61, 64, 67, 68, 77, 65, 80, 66]
        filtered_result = exception_filter.filter_sudden_change(heart_rates)
        self.assertEqual(filtered_result, [60, 61, 64, 67, 68, 65, 66])

    def test_filter_exception_results_two(self):
        """
        try threshold set to 0.2
        """
        exception_filter = ExceptionFilter(0.20)
        heart_rates = [60, 61, 64, 67, 68, 77, 65, 80, 66]
        filtered_result = exception_filter.filter_sudden_change(heart_rates)
        self.assertEqual(filtered_result, [60, 61, 64, 67, 68, 77, 65, 66])

    def test_set_threshold(self):
        exception_filter = ExceptionFilter(0.12)
        self.assertEqual(exception_filter.threshold, 0.12)
