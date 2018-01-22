import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

from auxiliary.data_manager import DataManager
from signals_process_tools.background_remover import BackGroundRemover

sns.set()
np.random.seed(0)
fig = plt.figure()

# background remove
background_remover = BackGroundRemover()

data_manager = DataManager()
data = data_manager.load(
    scenario='experiment_20cm_post_squat_95',
    path='../../data_collection')

# read data
raw_signals = np.array([data['walabot']][0])
print(len(raw_signals))
raw_signals = background_remover.remove(raw_signals)
print(len(raw_signals))
raw_signals = np.transpose(raw_signals)
# plt.plot(raw_signals[156])
# plt.show()
print(len(raw_signals))
cmap = sns.cubehelix_palette(32)
ax = sns.heatmap(raw_signals[0:1000], cmap=cmap)
fig.add_axes(ax)
plt.show()
