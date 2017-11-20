#!/usr/bin/python

""" Complete the code in ClassifyNB.py with the sklearn
    Naive Bayes classifier to classify the terrain data.

    The objective of this exercise is to recreate the decision
    boundary found in the lesson video, and make a plot that
    visually shows the decision boundary """

from prep_terrain_data import makeTerrainData
from class_vis import prettyPicture, output_image
from ClassifyNB import classify
from sklearn.metrics import accuracy_score
from PIL import Image
from time import time
import pprint
import numpy as np
import pylab as pl
import sys
import matplotlib.pyplot as plt
import copy



features_train, labels_train, features_test, labels_test = makeTerrainData(1000)
# pprint.pprint(features_train)
# pprint.pprint(labels_train)
# pprint.pprint(features_test)
# pprint.pprint(labels_test)

### the training data (features_train, labels_train) have both "fast" and "slow" points mixed
### in together--separate them so we can give them different colors in the scatterplot,
### and visually identify them
grade_fast = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii] == 0]
bumpy_fast = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii] == 0]
grade_slow = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii] == 1]
bumpy_slow = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii] == 1]


########################## SVM #################################
### we handle the import statement and SVC creation for you here
from sklearn.svm import SVC
clf = SVC(kernel='rbf', C=10000.0)
t0 = time()
clf.fit(features_train, labels_train)
print ("training time:", round(time() - t0, 3), "s")
t0 = time()
pred = clf.predict(features_test)
print ("predict time:", round(time() - t0, 3), "s")
accuracy = accuracy_score(labels_test, pred)
print (accuracy)

#### now your job is to fit the classifier
#### using the training features/labels, and to
#### make a set of predictions on the test data
#### store your predictions in a list named pred


## draw the decision boundary with the text points overlaid
prettyPicture(clf, features_test, labels_test)
output_image("test.png", "png", open("test.png", "rb").read())

img = Image.open('test.png')
img.show()

