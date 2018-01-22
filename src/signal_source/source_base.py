import abc
import time


class SignalSourceBase:
    __metaclass__ = abc.ABCMeta

    def __init__(self):
        self.count = 0
        self.window_length = 0
        self.if_start_set = True
        self.start = 0

    @abc.abstractclassmethod
    def get(self):
        """
        :return: A set of signals
        :rtype: A list
        """
        return None

    def get_sample_rate(self):
        """
          ..warn:: The function shall be called after per windows length, and it will reset the count to zero

          Implementing this function requires to add "self.count += 1" in get()
          """
        sample_rate = self.count / self.window_length
        self.count = 0
        return sample_rate

    def if_continue(self):
        """
        The start time will be initialized as soon as the if_continue is called
        """
        self.set_start_time()
        if time.time() - self.start < self.window_length:
            return True
        else:
            return False

    def set_start_time(self):
        if self.if_start_set:
            self.start = time.time()
            self.if_start_set = False
