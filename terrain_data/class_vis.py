#!/usr/bin/python

# from udacityplots import *
import warnings

warnings.filterwarnings("ignore")

import matplotlib

matplotlib.use('agg')

import matplotlib.pyplot as plt
import pylab as pl
import numpy as np

from PIL import Image
import io

# plt.ioff()

def prettyPicture(clf, X_test, y_test):
    x_min = 0.0;
    x_max = 1.0
    y_min = 0.0;
    y_max = 1.0

    # Plot the decision boundary. For that, we will assign a color to each
    # point in the mesh [x_min, m_max]x[y_min, y_max].
    h = .01  # step size in the mesh
    xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))
    # print (xx)
    # print (yy)
    # print (xx.ravel())
    # print (yy.ravel())
    Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])
    # print (Z)

    # # Put the result into a color plot
    # print (type(xx))
    Z = Z.reshape(xx.shape)
    # print (Z)
    plt.xlim(xx.min(), xx.max())
    plt.ylim(yy.min(), yy.max())

    plt.pcolormesh(xx, yy, Z, cmap=pl.cm.seismic)

    # Plot also the test points
    grade_sig = [X_test[ii][0] for ii in range(0, len(X_test)) if y_test[ii] == 0]
    bumpy_sig = [X_test[ii][1] for ii in range(0, len(X_test)) if y_test[ii] == 0]
    grade_bkg = [X_test[ii][0] for ii in range(0, len(X_test)) if y_test[ii] == 1]
    bumpy_bkg = [X_test[ii][1] for ii in range(0, len(X_test)) if y_test[ii] == 1]

    plt.scatter(grade_sig, bumpy_sig, color="b", label="fast")
    plt.scatter(grade_bkg, bumpy_bkg, color="r", label="slow")
    plt.legend()
    plt.xlabel("bumpiness")
    plt.ylabel("grade")

    plt.savefig("test.png")
# from ClassifyNB import classify
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
# features_test = [[0.08693883262941615, 0.5892656838759087],
#                  [0.4219218196852704, 0.8094304566778266],
#                  [0.029797219438070344, 0.006498759678061017]]
#
# labels_test = [0.0, 1.0, 0.0]
# clf = classify(features_train, labels_train)
# # print (clf)
#
# prettyPicture(clf, features_test, labels_test)


import base64
import json
import subprocess


def output_image(name, format, bytes):
    image_start = "BEGIN_IMAGE_f9825uweof8jw9fj4r8"
    image_end = "END_IMAGE_0238jfw08fjsiufhw8frs"
    data = {}
    data['name'] = name
    data['format'] = format
    data['bytes'] = base64.encodestring(bytes)
    print (image_start + json.dumps(data) + image_end)



def show(bytes):
    image_data = bytes
    image = Image.open(io.BytesIO(image_data))
    image.show()

