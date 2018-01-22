import unittest

from signals_process_tools.static_filter import StdStaticFilter


class TestStaticFilter(unittest.TestCase):

    def setUp(self):
        # self.mock_signals = [[[1, 2, 3, 4, 5],
        #                       [10, 10, 4, 5, 6]],
        #                      [[1, 2, 3, 4, 5],
        #                       [10, 10, 4, 5, 6]]
        #                      ]
        self.mock_signals = {
            '1_11': [[1, 2, 3, 4, 5], [10, 10, 4, 5, 6]],
            '1_4': [[1, 2, 3, 4, 5], [10, 10, 4, 5, 6]]
        }
        self.static_filter = StdStaticFilter()

    def test_filter_one_candidates(self):
        """
        refer to the data format of the return value to know why [0][1][0]
        :return:
        """
        result = self.static_filter.filter(self.mock_signals, 1)
        self.assertListEqual(
            [1, 10]
            ,
            result['1_11']['0'].tolist()
        )
        self.assertListEqual(
            [1, 10]
            ,
            result['1_4']['0'].tolist()
        )

    def test_filter_multiple_candidates(self):
        static_filter = StdStaticFilter()
        result = static_filter.filter(self.mock_signals, 2)
        self.assertListEqual(
            [2, 10]
            ,
            result['1_11']['1'].tolist()
        )

        self.assertListEqual(
            [2, 10]
            ,
            result['1_4']['1'].tolist()
        )
