#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle
import pprint
import re

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))
# pprint.pprint (enron_data)
print (len(enron_data))
# pprint.pprint (enron_data['GLISAN JR BEN F'])
# print (type(enron_data['GLISAN JR BEN F']['salary']))
# print (type(enron_data['GLISAN JR BEN F']['salary']) == int)
# print (enron_data['PRENTICE JAMES']['total_stock_value'])
# print (enron_data['COLWELL WESLEY']['from_this_person_to_poi'])
# pprint.pprint (enron_data['SKILLING JEFFREY K']['total_payments'])
# pprint.pprint (enron_data['FASTOW ANDREW S']['total_payments'])
# pprint.pprint (enron_data['LAY KENNETH L']['total_payments'])
# no_of_features = len(enron_data[enron_data.keys()[0]])
# print (no_of_features)
count_salary = 0
count_email = 0

# emails = re.findall(r'[\w\.-]+@[\w\.-]+', str)

for element in enron_data:
    print (enron_data[element]['email_address'])
    # if enron_data[element]['email_address'] is emails:
    #     print enron_data[element]['email_address']
    # if (type(enron_data[element]['salary']) == int):
    #     count_salary += 1
    if (enron_data[element]['email_address']) != 'NaN':
        count_email += 1
# print ("count salary = ", count_salary)
print ("count email = ", count_email)
    # if type(enron_data[element]['salary']) == True:



def isValidEmail(email):
 if len(email) > 7:
    if re.match("^.+@([?)[a-zA-Z0-9-.]+.([a-zA-Z]{2,3}|[0-9]{1,3})(]?)$", email) != None:
        return True
 return False

isValidEmail("asffafs")