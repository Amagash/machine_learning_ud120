from time import time
def classify(features_train, labels_train):
    ### import the sklearn module for GaussianNB
    ### create classifier
    ### fit the classifier on the training features and labels
    ### return the fit classifier

    from sklearn.naive_bayes import GaussianNB
    clf = GaussianNB()
    # print (clf)
    t0 = time()
    fitting = clf.fit(features_train, labels_train)
    print "training time:", round(time() - t0, 3), "s"
    # print (pred)
    return fitting
    ### your code goes here!



#

#
# features_train = [[0.6394267984578837, 0.21863797480360336],
#                  [0.025010755222666936, 0.5053552881033624],
#                  [0.27502931836911926, 0.026535969683863625],
#                  [0.22321073814882275, 0.1988376506866485],
#                  [0.7364712141640124, 0.6498844377795232],
#                  [0.6766994874229113, 0.5449414806032167],
#                  [0.8921795677048454, 0.2204406220406967]]
#
# labels_train = [1.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0]
#
# classify(features_train, labels_train)