from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

import numpy as np
import pandas.plotting as pdplot
# from sklearn.linear_model import Ridge

def classification_iris_concrete(axesGrid=None, classifier=None):

    if classifier is None:
        raise Exception("classifierMixin from sklearn must not be null")

    bunch = load_iris()

    print("bunch.target_names={}".format(bunch.target_names))

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

    # plt.show()


def classification_generic(data, target, classifier=None):
    """
    Shuffles test data and scores classification algorithm.

    =================   ==============
    Classes                          3
    Samples per class               50
    Samples total                  150
    Dimensionality                   4
    Features            real, positive
    =================   ==============


    Parameters
    ----------
    data : numpy array, panda DataFrame.
        Contains 2d matrix containing data-

    target : numpy array, panda DataFrame
        Contains target labels

    target_names : pandas Series containing label values with label names as index



    Returns
    -------

    Notes
    -----
    """

    X_train, X_test, y_train, y_test = train_test_split(data, target, random_state=0)

    #npY_train = y_train.iloc[:,0].ravel()   # get Series of column 0 and male to np array
    # npY_test  = y_test.iloc[:,0].ravel()   # get Series of column 0 and male to np array

    # print("target_names={}".format(target_names))
    print("feature_namee={}".format(data.columns))
    print("X_train.shape={}".format(X_train.shape))
    print("y_train.shape={}".format(y_train.shape))

    # X_train_width_only = np.hstack((np.reshape(X_train[:,1], (-1, 1)), np.reshape(X_train[:,3], (-1, 1))))
    # print("X_train_width_only.shape={}".format(X_train_width_only.shape))

    classifier.fit(X_train, y_train.iloc[:, 0])
    print("Score train={:.2f}".format(classifier.score(X_train, y_train.iloc[:, 0])))
    print("Score test={:.2f}".format(classifier.score(X_test, y_test.iloc[:, 0])))

    # print("[n_samples, Predict proba per class + y_test labels]={}".format(np.hstack((classifier.predict_proba(X_test), y_test))))

    # plot
    # plot2d.plot_2d_separator(alg, X_train, ax=axesGrid)

    # plt.show()






