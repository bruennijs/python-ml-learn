from pandas import DataFrame, Series
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier

import mlhelpers.converter as conv
import matplotliblearn.classification as mplclassification
import classification.iris as class_iris
from sklearn.datasets import load_iris
import numpy as np
from strava_api.strava import StravaApiClient
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

dfIrisSeaborn = sb.load_dataset('iris')

print("dfIrisSeaborn={}".format(dfIrisSeaborn))

# slice vertically and use only two features and label 'species'
dfDataSepals, sTarget = conv.sliceVertically(dfIrisSeaborn, {'sepal_length', 'sepal_width'}), dfIrisSeaborn['species']
#sFeatures = Series(data=np.arange(0, 7), index=feature_names)
#print("features={}".format(sFeatures))

pairGrid = mplclassification.pairplot(dfDataSepals.assign(species=sTarget), 'species')

# convert to numpy
# npSepals = dfSepals.to_numpy(copy=True)

# plot pair plot of all features
plt.show()

strategy = KNeighborsClassifier(n_neighbors=3)
# classification with logistic regression
# strategy = LogisticRegression(C=1)

# class_iris.classification_iris_concrete(pairGrid.axes, classifier=strategy)
class_iris.classification_generic(data=dfIrisSeaborn.iloc[:, 0:4], target=DataFrame({"species": sTarget}), axesGrid=pairGrid.axes, classifier=strategy)
# print("Coef={}".format(strategy.coef_))

# strava api
client = StravaApiClient()
client.loadLoggedInUsersActivities()













