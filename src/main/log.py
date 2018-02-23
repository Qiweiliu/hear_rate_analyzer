import os.path
import numpy as np
import pprint


def log(folder_path, file_name, heart_rates):
    flag = os.path.isfile(folder_path + '/' + 'oximeter.npy')
    if flag is True:
        oximeter_dict = np.load(folder_path + '/' + 'oximeter.npy').item()
        # noinspection PyUnresolvedReferences
        oximeter_dict[file_name] = heart_rates
        np.save(folder_path + '/' + 'oximeter.npy', oximeter_dict)
        pprint.pprint(oximeter_dict)
    else:
        oximeter_dict = {file_name: heart_rates}
        np.save(folder_path + '/' + 'oximeter.npy', oximeter_dict)
        pprint.pprint(oximeter_dict)


if __name__ == '__main__':
    log(folder_path='../../data_collection',
        file_name='IPhone_Length_STATIC_NARROW_5',
        heart_rates=[51]
        )
