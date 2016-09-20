#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    
    cleaned_data = []

    ### your code goes here

    # Calculate the error. This will serve to sort and select the cleaned data
    errors = list((net_worths - predictions)**2)

    cleaned_data = zip(ages, net_worths, errors)

    # see [https://wiki.python.org/moin/HowTo/Sorting] student sorted by age
    # exemple.
    cleaned_data = sorted(cleaned_data, key=lambda data: data[2])

    # Clean away the 10% of points that have the largest residual errors
    cleaned_data = cleaned_data[:80]


    
    return cleaned_data

