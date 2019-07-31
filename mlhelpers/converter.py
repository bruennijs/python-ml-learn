import numpy as np
import pandas as pd

def from_X_y_to_DataFrame(X, y, column_names):

    y_2d = y.reshape(-1, 1)    # make 1-d array to 2-d with 1 column to match X vector
    #X_join_y_array = np.concatenate((X, y_2d), axis=1)
    X_join_y_array = np.hstack((X, y_2d))
    return pd.DataFrame(X_join_y_array, columns=column_names, copy=True)
