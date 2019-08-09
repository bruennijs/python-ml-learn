from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import  LogisticRegression
from sklearn.svm import LinearSVC
import matplotlib.pyplot as plt
import sklearn.neighbors.classification as knn
import mglearn.plot_2d_separator as plot2d

import numpy as np
import pandas.plotting as pdplot
# from sklearn.linear_model import Ridgeplot2d

def classification_generic(axesGrid=None, classifier=None):

    if classifier is None:
        raise Exception("classifierMixin from sklearn must not be null")

    bunch = load_iris()

    X_train, X_test, y_train, y_test = train_test_split(bunch.data, bunch.target, random_state=0)

    category = np.where(bunch.target_names == 'versicolor')[0]

    print("target_names={}".format(bunch.target_names))
    print("feature_namee={}".format(bunch.feature_names))
    print("X_train.shape={}".format(X_train.shape))
    print("y_train.shape={}".format(y_train.shape))

    # X_train_width_only = np.hstack((np.reshape(X_train[:,1], (-1, 1)), np.reshape(X_train[:,3], (-1, 1))))
    # print("X_train_width_only.shape={}".format(X_train_width_only.shape))

    classifier.fit(X_train, y_train == category)
    print("Score train={:.2f}".format(classifier.score(X_train, y_train == category)))
    print("Score test={:.2f}".format(classifier.score(X_test, y_test == category)))

    # plot
    # plot2d.plot_2d_separator(alg, X_train, ax=axesGrid)

    plt.show()







