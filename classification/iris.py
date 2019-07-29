from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
import pandas.plotting as pdplot
import matplotlib.pyplot as plt
import matplotliblearn.classification
from sklearn.linear_model import Ridge

def ridge():

    iris_dataset = load_iris()
    X_train, X_test, y_train, y_test = train_test_split(iris_dataset['data'], iris_dataset['target'], random_state=0)

    print("iris_dataset keys={}".format(iris_dataset.keys()))
    print("iris_dataset.len={}".format(len(iris_dataset['data'])))
    print("X_train.len={}".format(len(X_train)))

    ridge = Ridge()
    ridge.fit(X_train, y_train)
    print("Score test={:.2f}".format(ridge.score(X_test, y_test)))

    # plot test split


    plt.show()







