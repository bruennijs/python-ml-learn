from mglearn.plot_2d_separator import plot_2d_separator, plot_2d_classification
from pandas import DataFrame, Series
from sklearn.linear_model import LogisticRegression, Lasso
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC, LinearSVC

import mlhelpers.converter as conv
import matplotliblearn.classification as mplclassification
import classification.iris as class_iris
from sklearn.datasets import load_iris

from strava_api import StravaApiClient
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

# strategy = KNeighborsClassifier(n_neighbors=3)
strategy = LinearSVC(C=0.001, max_iter=100000)
# strategy = SVC(C=1000)
# classification with logistic regression
# strategy = LogisticRegression(C=1)

# class_iris.classification_iris_concrete(pairGrid.axes, classifier=strategy)
class_iris.classification_generic(data=dfIrisSeaborn.iloc[:, 0:4], target=DataFrame({"species": sTarget}) == 'versicolor', classifier=strategy)
# print("strategy.classes_={}".format(strategy.classes_))
print("Coef={}".format(strategy.coef_))

# plot pair plot of all features
pairGrid = mplclassification.pairplot(dfIrisSeaborn.assign(species=sTarget), 'species')

# plot 2d seperator with linear classificatos having coefs_ vector
# plot_2d_separator(strategy, dfIrisSeaborn.iloc[:, 0:2].to_numpy(copy=True))

# plot
plt.show()


# strava api
# client = StravaApiClient()
# client.loadLoggedInUsersActivities()
# client.get_Profile()













