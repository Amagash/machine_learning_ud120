#!/usr/bin/python

import pickle
import sys
import matplotlib.pyplot
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit
import pprint


### read in data dictionary, convert to numpy array
data_dict = pickle.load( open("../final_project/final_project_dataset.pkl", "r") )
# pprint.pprint(data_dict)

pprint.pprint(data_dict['TOTAL'])

data_dict.pop('TOTAL')
# pprint.pprint(data_dict['TOTAL'])
pprint.pprint(data_dict)

features = ["salary", "bonus"]
# print features
data = featureFormat(data_dict, features)
highest_salary = 0
person_salary = ''
highest_bonus = 0
person_bonus = ''

for name in data_dict:
    # float() does not include NaN values
    bonus = float(data_dict[name]["bonus"])
    salary = float(data_dict[name]["salary"])
    if bonus >= 5000000 and salary >= 1000000:
        print name, "bonus: ", data_dict[name]["bonus"], "salary: ", data_dict[name]["salary"]

### your code below
for point in data:
    salary = point[0]
    bonus = point[1]
    matplotlib.pyplot.scatter( salary, bonus )

matplotlib.pyplot.xlabel("salary")
matplotlib.pyplot.ylabel("bonus")
matplotlib.pyplot.show()


