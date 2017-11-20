#!/usr/bin/python
import random
import pprint


def makeTerrainData(n_points):
###############################################################################
### make the toy dataset

    random.seed(42)
    grade = [random.random() for ii in range(0,n_points)]
    bumpy = [random.random() for ii in range(0,n_points)]
    error = [random.random() for ii in range(0,n_points)]
    # pprint.pprint(grade)
    # print ("")
    # pprint.pprint(bumpy)
    # print ("")
    # pprint.pprint(error)
    # print ("")
    y = [round(grade[ii]*bumpy[ii]+0.3+0.1*error[ii]) for ii in range(0,n_points)]
    for ii in range(0, len(y)):
        if grade[ii]>0.8 or bumpy[ii]>0.8:
            y[ii] = 1.0
    # print (y)

### split into train/test sets
    X = [[gg, ss] for gg, ss in zip(grade, bumpy)]
    # print ("X = ")
    # pprint.pprint (X)
    split = int(0.75*n_points)
    # print (split)
    X_train = X[0:split]
    # print ("X_train = ")
    # pprint.pprint (X_train)
    # print ("")
    X_test  = X[split:]
    # print ("X_test = ")
    # pprint.pprint(X_test)
    # print ("")
    y_train = y[0:split]
    # print ("y_train = ")
    # pprint.pprint(y_train)
    # print ("")
    y_test  = y[split:]
    # print ("y_test = ")
    # pprint.pprint(y_test)
    # print ("")

    grade_sig = [X_train[ii][0] for ii in range(0, len(X_train)) if y_train[ii]==0]
    # pprint.pprint(grade_sig)
    bumpy_sig = [X_train[ii][1] for ii in range(0, len(X_train)) if y_train[ii]==0]
    # pprint.pprint(bumpy_sig)
    grade_bkg = [X_train[ii][0] for ii in range(0, len(X_train)) if y_train[ii]==1]
    bumpy_bkg = [X_train[ii][1] for ii in range(0, len(X_train)) if y_train[ii]==1]

    training_data = {"fast":
                         {"grade":grade_sig, "bumpiness":bumpy_sig},
                     "slow":
                         {"grade":grade_bkg, "bumpiness":bumpy_bkg}
                     }

    # pprint.pprint(training_data)

    grade_sig = [X_test[ii][0] for ii in range(0, len(X_test)) if y_test[ii]==0]
    bumpy_sig = [X_test[ii][1] for ii in range(0, len(X_test)) if y_test[ii]==0]
    grade_bkg = [X_test[ii][0] for ii in range(0, len(X_test)) if y_test[ii]==1]
    bumpy_bkg = [X_test[ii][1] for ii in range(0, len(X_test)) if y_test[ii]==1]

    test_data = {"fast":
                     {"grade":grade_sig, "bumpiness":bumpy_sig},
                 "slow":
                     {"grade":grade_bkg, "bumpiness":bumpy_bkg}
                 }

    # pprint.pprint(test_data)

    return X_train, y_train, X_test, y_test
    # return training_data, test_data

# pprint.pprint(makeTerrainData(10))