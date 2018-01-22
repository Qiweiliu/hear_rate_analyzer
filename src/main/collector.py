import serial

from auxiliary.data_manager import DataManager
from signal_source.arduino_signals import Arduino
from signal_source.walabot_socket import WalabotSocket
from signals_process_tools.signal_getter import SignalGetter


class Collector:
    def __init__(self, scenario, window_length):
        self.arduino_getter = SignalGetter()
        self.walabot_getter = SignalGetter()
        self.scenario = scenario
        self.walabot_output = []
        self.arduino_output = []
        self.window_length = window_length

    def start_collect(self):
        self.set_up_walabot()
        # self.set_up_arduino()
        self.run()
        return self.walabot_output, self.arduino_output

    def set_up_walabot(self):
        walabot_source = WalabotSocket(sample_number=12288,
                                       type_of_size=8,
                                       window_length=
                                       self.window_length
                                       )
        self.walabot_getter.set_signal_source(walabot_source)

    # def set_up_arduino(self):
    #     # arduino_source = Arduino(serial.Serial('COM3', 115200),
    #     #                          window_length=
    #     #                          self.window_length)
    #     self.arduino_getter.set_signal_source(arduino_source)

    def run(self):
        self.walabot_output = self.walabot_getter.start()
        # self.arduino_output = self.arduino_getter.start()


if __name__ == '__main__':
    # start collect
    collector = Collector(scenario='test',
                          window_length=10)
    outputs = collector.start_collect()

    # save data
    data_manager = DataManager()
    data_manager.save(scenario='a_test',
                      walabot_signals=outputs[0][0],
                      arduino_signals=None,
                      sample_rate=outputs[0][1],
                      path='../../data_collection')
