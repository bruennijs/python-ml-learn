import mglearn
import mglearn.plot_2d_separator as plot2d
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
sTarget = dfIrisSeaborn['species']

print("dfIrisSeaborn={}".format(dfIrisSeaborn))

# slice vertically and use only two features and label 'species'
#sFeatures = Series(data=np.arange(0, 7), index=feature_names)

# strategy = KNeighborsClassifier(n_neighbors=3)
# strategy = LinearSVC(C=0.1, max_iter=100000)
strategy = SVC(C=10, gamma=0.1)
# classification with logistic regression
# strategy = LogisticRegression(C=0.1)

# train & score
#class_iris.classification_generic(data=dfIrisSeaborn.iloc[:, 0:4], target=DataFrame({"species": sTarget}) == 'versicolor', classifier=strategy)
dfNfeatures = dfIrisSeaborn.loc[:, ('sepal_length', 'petal_length')]

class_iris.classification_generic(data=dfNfeatures, target=DataFrame({"species": sTarget}) == 'versicolor', classifier=strategy)


# print("strategy.classes_={}".format(strategy.classes_))
# print("Coef={}".format(strategy.coef_))

# plot pair plot of all features
pairGrid = mplclassification.pairplot(dfNfeatures.assign(species=sTarget), 'species')

# plot 2d seperator with linear classificatos having coefs_ vector
# axes = plt.subplots(2)
plot2d.plot_2d_separator(strategy, dfNfeatures.to_numpy(copy=True), ax=pairGrid.axes[0, 1])
plot2d.plot_2d_separator(strategy, dfNfeatures.to_numpy(copy=True), ax=pairGrid.axes[1, 0])
# mglearn.discrete_scatter(dfNfeatures.iloc[:, 0], dfNfeatures.iloc[:, 1], sTarget)

# plot
plt.show()


# strava api
# client = StravaApiClient()
# client.loadLoggedInUsersActivities()
# client.get_Profile()













