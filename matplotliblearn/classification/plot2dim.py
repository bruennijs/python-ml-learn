import matplotlib.pyplot as plt
from sklearn.datasets import load_iris as load_dataset
import numpy as np


def plot1feature_manually():
    dataset = load_dataset()
    data = dataset['data']
    target = dataset['target']
    feature_names = dataset['feature_names']


    n_rows, n_features = np.shape(data)
    print ("features={}".format(n_features))

    fig, axes = plt.subplots(1, n_features, figsize=(4*n_features, 4))

    print("max feature0={}".format(np.max(data[:, 0])))

    # axes[0, 0].plot(data[:, 0], data[:, 1], 'bo') # no lines, markers
    # axes[0, 1].plot(data[:, 0], data[:, 2])

    # labeled scatter
    for feature_index in range(0, n_features):
        print ("i={}".format(feature_index))
        axes[feature_index].scatter(data[:, 0], data[:, feature_index], c=target, cmap="viridis") # no lines, markers
        axes[feature_index].set_xlabel(feature_names[0])
        axes[feature_index].set_ylabel(feature_names[feature_index])
    plt.show()

def plot_linear_func(axes, x_left, x_right, m, b):
    X_vector = np.linspace(x_left, x_right, np,abs(x_left) + np.abs(x_right))
    axes.plot(X_vector, m*X_vector + b, "-b")
