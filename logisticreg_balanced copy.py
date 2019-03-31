import pandas as pd
import numpy as np
from sklearn import datasets, linear_model
from sklearn.linear_model import LogisticRegression
import statsmodels.api as sm
from scipy import stats
from sklearn.model_selection import train_test_split
from sklearn.utils import resample
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2


##################################
########## SETTINGS ##############
##################################

# which SNP file to load
d=np.load('xs_ys_4.npz')

##################################
##################################


xs = d['xs']
ys = d['ys']


xs_0 = xs[np.where(ys==0)[0],:]
xs_1 = xs[np.where(ys==1)[0],:]
ys_0 = ys[np.where(ys==0)[0]]
ys_1 = ys[np.where(ys==1)[0]]

num_in_majority_class = max(len(ys_0),len(ys_1))

xs_0, ys_0 = resample(xs_0,ys_0,replace=True,n_samples=num_in_majority_class)
xs_1, ys_1 = resample(xs_1,ys_1,replace=True,n_samples=num_in_majority_class)

xs = np.vstack((xs_0,xs_1))
ys = np.hstack((ys_0, ys_1))



# logistic regression here

# example with sklearn

X_train, X_test, y_train, y_test = train_test_split(xs, ys, test_size=0.20)
"""
clf = LogisticRegression(random_state=0, solver='lbfgs').fit(X_train, y_train)
print clf.score(X_train,y_train)
print clf.score(X_test,y_test)
"""


print X_train.shape
X_new = SelectKBest(chi2, k=100).fit_transform(X_train, y_train)
print X_new.shape






