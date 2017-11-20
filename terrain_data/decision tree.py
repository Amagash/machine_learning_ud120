#!/usr/bin/python

""" lecture and example code for decision tree unit """

import sys
from class_vis import prettyPicture, output_image
from prep_terrain_data import makeTerrainData
from sklearn import tree
from sklearn.metrics import accuracy_score
from time import time
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
import pylab as pl
# from classifyDT import classify

features_train, labels_train, features_test, labels_test = makeTerrainData(1000)


def classify(features_train, labels_train, min_samples_split):
    ### your code goes here--should return a trained decision tree classifer
    clf = tree.DecisionTreeClassifier(min_samples_split=min_samples_split)
    t0 = time()
    fitting = clf.fit(features_train, labels_train)
    print "training time:", round(time() - t0, 3), "s"
    return fitting

### the classify() function in classifyDT is where the magic
### happens--fill in this function in the file 'classifyDT.py'!
clf50 = classify(features_train, labels_train, 50)
t0 = time()
pred50 = clf50.predict(features_test)
print ("predict time:", round(time() - t0, 3), "s")

acc_min_samples_split_50 = accuracy_score(labels_test, pred50)

clf2 = classify(features_train, labels_train, 2)
t0 = time()
pred2 = clf2.predict(features_test)
print ("predict time:", round(time() - t0, 3), "s")
acc_min_samples_split_2 = accuracy_score(labels_test, pred2)


#### grader code, do not modify below this line

# prettyPicture(clf, features_test, labels_test)
# output_image("test.png", "png", open("test.png", "rb").read())
#
# img = Image.open('test.png')
# img.show()

########################## DECISION TREE #################################


### your code goes here--now create 2 decision tree classifiers,
### one with min_samples_split=2 and one with min_samples_split=50
### compute the accuracies on the testing data and store
### the accuracy numbers to acc_min_samples_split_2 and
### acc_min_samples_split_50, respectively

def submitAccuracies():
  return {"acc_min_samples_split_2":round(acc_min_samples_split_2,3),
          "acc_min_samples_split_50":round(acc_min_samples_split_50,3)}
print (submitAccuracies())