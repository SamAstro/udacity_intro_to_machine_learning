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

import numpy as np
import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

# Number of people in the dataset
len(enron_data)

# For each person, how many features are available?
len(enron_data["SKILLING JEFFREY K"])

# How many POI are there?

counts_poi = 0

for k,d in enron_data.iteritems():
    if d['poi'] == True:
        counts_poi += 1

print 'There are that many poi in the dataset:', counts_poi

# HOw many POI are there in total

fid = open('../final_project/poi_names.txt', 'r')

lines = fid.readlines()

# Remove first two lines from the counts
print 'There are that many poi in total:', len(lines[2:])


# Here are the keys in the dataset (people)
print enron_data.keys()

# Here are the keys in one entry of the dataset
print enron_data["PRENTICE JAMES"].keys()

# Value of stock belonging to James Prentice
print enron_data["PRENTICE JAMES"]["total_stock_value"]

# Number of emails from Wesley Colwell to POI
print enron_data["COLWELL WESLEY"]["from_this_person_to_poi"]

# Value of stock option of Jeffrey K Skilling
print enron_data["SKILLING JEFFREY K"]["exercised_stock_options"]

print enron_data["SKILLING JEFFREY K"]["total_payments"]
print enron_data["LAY KENNETH L"]["total_payments"]
print enron_data["FASTOW ANDREW S"]["total_payments"]

counts_salary_email = np.array([0,0])

for k,d in enron_data.iteritems():
    if d['salary'] != 'NaN':
        counts_salary_email[0] += 1

    if d['email_address'] != 'NaN':
        counts_salary_email[1] += 1

print counts_salary_email

# Total percentage people with NaN in total_payment
counts_totpay_nan = 0.
counts_totpay_nan_poi = 0.
for k in enron_data.keys():
    if enron_data[k]["total_payments"] == 'NaN':
        counts_totpay_nan += 1
        if enron_data[k]["poi"] == True:
            counts_totpay_nan_poi += 1

print counts_totpay_nan
print counts_totpay_nan/len(enron_data.keys())

print counts_totpay_nan_poi
print counts_totpay_nan_poi/len(enron_data.keys())

print len(enron_data.keys()) + 10
