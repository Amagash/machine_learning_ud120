#!/usr/bin/python
import numpy as np
import pandas as pd
import pprint

def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    # df1 = df1.assign(e=p.Series(np.random.randn(sLength)).values)

    cleaned_data = []
    errors = abs(net_worths - predictions)
    cleaned_data = zip(ages, net_worths, errors)
    # pprint.pprint (cleaned_data)

    cleaned_data = sorted(cleaned_data, key=lambda x: x[2], reverse=False)
    # pprint.pprint (cleaned_data)
    # print (len(cleaned_data))
    cleaned_data = cleaned_data[0: int((0.9) * len(ages))]
    # pprint.pprint(cleaned_data)
    # print (len(cleaned_data))
    # limit = int(len(net_worths) * 0.1)

    # dict = {'prediction' : pd.Series(predictions),
    #         'age' : pd.Series(ages),
    #         'net_worth' : pd.Series(net_worths),
    #         }
    # # dict = {'prediction' : predictions,
    # #         'age' : ages,
    # #         'net_worth' : net_worths,
    # #         }
    # # print dict
    # # df = pd.DataFrame(columns = 'prediction', data =predictions, index=[0])
    # # print df
    # df = pd.DataFrame(dict, index=[0])
    # # print df
    #
    # error = []
    # for i in range(len(predictions)):
    #     errors = abs(df['prediction'][i] - df['net_worth'][i])
    #     error.append(errors)
    #
    # df['error'] = pd.Series(error)
    #
    # sorted = df.sort(['error'])
    #
    # sub = (sorted[0:int((0.9) * len(df))]).reset_index(drop=True)
    # for i in range(len(sub)):
    #     cleaned_data.append((sub['age'][i],
    #                          sub['net_worth'][i],
    #                          sub['error'][i]))
    return cleaned_data

# predictions = [23, 5,4657 ,56 ,7, 23,4, 345, 345, 234 ]
# ages = [23,5,45, 65,67,6,8 ,76, 897, 9]
# net_worths = [123234, 23432423, 435353, 435436, 6865756, 34657, 57577, 234345, 23435, 345346]
#
# pprint.pprint (outlierCleaner(predictions, ages, net_worths))