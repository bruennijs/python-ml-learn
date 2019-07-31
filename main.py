from mglearn.datasets import load_extended_boston
import mlhelpers.converter as conv
import matplotliblearn.classification as mplclassification
import classification.iris as class_iris
from sklearn.datasets import load_iris
import numpy as np
import strava
import seaborn as sb
import matplotlib.pyplot as plt

# numpy learn
# execute()

# skikit
#iris.ridge()

# matplotlib

dataset_bunch = load_iris()
npData = dataset_bunch['data']
npTarget = dataset_bunch['target']
feature_names = dataset_bunch['feature_names']

irisDataFrame = conv.from_X_y_to_DataFrame(npData, npTarget, np.hstack((feature_names, "species")))
irisDataFrameSeaborn = sb.load_dataset('iris')

# plot pair plot of all features
pairGrid = mplclassification.pairplot(irisDataFrameSeaborn, 'species')

# plot linear func of linear classification result using coef and intercept for corresponding feature
# mplclassification.plot_linear_func(pairGrid.axes[0, 1], 0.0, 8.0, 2.0, 1.0)
plt.show()

# classification with logistic regression
class_iris.logisticRegression(axesGrid=pairGrid.axes)

# strava api
print ("activities={}".format(strava.loadActivities()))


