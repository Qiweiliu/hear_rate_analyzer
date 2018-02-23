import os
import numpy as np
from auxiliary.data_manager import DataManager


class Batcher:

    def __init__(self, signal_processor, signal_preprocessor, signal_postprocessor):
        self.signal_preprocessor = signal_preprocessor
        self.signal_processor = signal_processor
        self.signal_postprocessor = signal_postprocessor

    def batcher_process(self, folder_path):
        result = {}
        file_names = os.listdir(folder_path)

        if '.DS_Store' in file_names:
            file_names.remove('.DS_Store')

        for file_name in file_names:
            file_name = os.path.splitext(file_name)[0]
            result[file_name] = self.start(file_name, folder_path).tolist()
        np.save(folder_path + '/' + 'current_directory_result.npy', result)
        return result

    def start(self, file_name, folder_path):
        # load data
        data_manager = DataManager()
        data = data_manager.load(
            scenario=file_name,
            path=folder_path)

        # read data
        raw_signals = [data['walabot']]
        sample_rate = data['sample_rate']

        # initialize sample_rate

        filtered_dynamic_signals = self.signal_preprocessor.preprocess(raw_signals, sample_rate)
        processed_result = self.signal_processor.process(filtered_dynamic_signals, sample_rate)
        heart_rates = self.signal_postprocessor.post_process(processed_result, sample_rate)
        return heart_rates

# if __name__ == '__main__':
#     batcher = Batcher()
#     batcher.batcher_process('../../data_collection')
