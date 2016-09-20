#!/usr/bin/python

import pickle
import sys
import matplotlib.pyplot
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit


### read in data dictionary, convert to numpy array
data_dict = pickle.load( open("../final_project/final_project_dataset.pkl", "r") )
features = ["salary", "bonus"]

# Looks like the outlier numbers match that of the total in the pdf file. Let's
# check that

print data_dict['TOTAL']['salary']
print data_dict['TOTAL']['bonus']
# Outputs :
#   26704229
#   97343619
# We have a match.


# Remove the outlier
data_dict.pop('TOTAL', 0)

data = featureFormat(data_dict, features)


### your code below

# Look for the bandits
for k, v in data_dict.iteritems():
    if data_dict[k]['salary'] == 'NaN' or data_dict[k]['bonus'] == 'NaN':
        pass
    else:
        if data_dict[k]['bonus'] >= 5e6 and data_dict[k]['salary'] >= 1e6:
            print k
            print data_dict[k]['bonus']
            print data_dict[k]['salary']


for point in data:
    salary = point[0]
    bonus = point[1]
    matplotlib.pyplot.scatter( salary, bonus )

matplotlib.pyplot.xlabel("salary")
matplotlib.pyplot.ylabel("bonus")
matplotlib.pyplot.show()
