#!/usr/bin/python


"""
    Starter code for the evaluation mini-project.
    Start by copying your trained/tested POI identifier from
    that which you built in the validation mini-project.

    This is the second step toward building your POI identifier!

    Start by loading/formatting the data...
"""

import pickle
import sys
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit
from sklearn.model_selection import train_test_split
from sklearn import tree
from sklearn.metrics import accuracy_score, precision_score, recall_score

data_dict = pickle.load(open("../final_project/final_project_dataset.pkl", "r") )

### add more features to features_list!
features_list = ["poi", "salary"]

data = featureFormat(data_dict, features_list)
labels, features = targetFeatureSplit(data)

### your code goes here 

features_train, features_test, labels_train, labels_test = train_test_split(
    features, labels, test_size=0.3, random_state=42)

clf = tree.DecisionTreeClassifier()
clf.fit(features_train, labels_train)


count_test = 0
for test in labels_test:
    if test == 1:
        count_test += 1
print ("count_test :", count_test)
print ("accuracy: ", (1- float(4)/float(29)))

pred = clf.predict(features_test)

print ("len pred: ", len(pred))

count = 0
for prediction in pred:
    if prediction == 1:
        count +=1
print ("count_pred : ", count)

for i in range(len(pred)):
    if pred[i]==1 and labels_test[i]==1:
        print "YES"

# print ("labels_test :", labels_test)
# print ("pred :", pred)
print ("precision", precision_score(labels_test, pred))
print ("recall", recall_score(labels_test, pred))

accuracy = accuracy_score(labels_test, pred)
print ("accuracy :", accuracy)