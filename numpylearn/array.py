import numpy as np;

def execute():
    array2dim = np.array([[1, 1], [2, 3], [3, 4]])
    print("mean y0={}".format(array2dim.mean((0, 1), keepdims=True)))

    print("mean y0={}".format(np.mean(array2dim, axis=0)))

    # array aggregations and calculations
    # y0 : meters from start
    # y1 : height in meters over ocean zero
    vector = np.array([[100, 1000], [200, 1014], [300, 1020]])
    vDistDiff = vector[1:, 0] - vector[0:2, 0]
    vHeightDiff = vector[1:, 1] - vector[0:2, 1]


    print ("vDist={}".format(vector))
    print ("vDistanceDiff={}".format(vDistDiff.reshape(-1, 1)))
    print ("vHeightDiff={}".format(vHeightDiff.reshape(-1, 1)))

    vDiff = np.concatenate((vDistDiff.reshape(-1, 1), vHeightDiff.reshape(-1, 1)), axis=1)
    vGradient = vDiff[:,1] / vDiff[:,0]
    print ("vDiff={}".format(vDiff))
    print ("vGradient={}".format(vGradient))

    vDiffMean = np.mean(vDiff, axis=0)
    vMeanDeltaX, vDeltaHeightMean = vDiffMean # copy elements starting at index 0 to variables
    print ("vDeltaHeightMean={}".format(vDeltaHeightMean))

    vDiffStd = np.std(vDiff, axis=0)
    print ("vDeltaHeightStd={}".format(vDiffStd))
