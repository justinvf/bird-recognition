# make sure packages are available
import matplotlib
import numpy
import scipy
import sklearn
import pandas

import submission_utils
import FoldBuilder
import wav_utils
import data
import transform
import classifier
import config

# check for elements added in sklearn 0.14
try:
    from sklearn.ensemble import AdaBoostRegressor
except ImportError:
    print("Error: sklearn 0.14 required, you have {0}".format(sklearn.__version__))
