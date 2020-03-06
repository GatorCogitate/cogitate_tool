# This import fixes a linting error with old division.
from __future__ import division
import numpy as np
import pandas as pd

# fake data
github_data = {
    "noorbuchi": {"COMMITS": 28, "ADDED": 349, "REMOVED": 70, "MODIFIED": 419},
    "bagashvilit": {"COMMITS": 22, "ADDED": 355, "REMOVED": 56, "MODIFIED": 411},
    "Jordan-A": {"COMMITS": 23, "ADDED": 375, "REMOVED": 43, "MODIFIED": 418},
    "WonjoonC": {"COMMITS": 27, "ADDED": 365, "REMOVED": 67, "MODIFIED": 432},
    "Hannah Schultz": {"COMMITS": 25, "ADDED": 315, "REMOVED": 75, "MODIFIED": 390},
    "Alexander_Hamilton": {"COMMITS": 41, "ADDED": 350, "REMOVED": 54, "MODIFIED": 404},
    "Karl_Marx": {"COMMITS": 0, "ADDED": 0, "REMOVED": 0, "MODIFIED": 0},
    "Julius_Caesar": {"COMMITS": 25, "ADDED": 363, "REMOVED": 35, "MODIFIED": 398},
    "Napoleon_Bonaparte": {"COMMITS": 24, "ADDED": 540, "REMOVED": 2, "MODIFIED": 542},
    "Alexander_the_Great": {"COMMITS": 42, "ADDED": 355, "REMOVED": 50, "MODIFIED": 405},
}


def calculate_iqr():
    list_numbers = [32, 37, 34, 35, 33, 35, 33, 32, 4, 2, 55, 74, 102]
    dataset = list_numbers
    below_iqr = []
    above_iqr = []
    within_iqr = []
    # sort the dataset in ascending order
    sorted(dataset)
    # determine the first and third quartiles
    q1, q3 = np.percentile(dataset,[25,75])
    # calculate the interquartile range (q3-q1)
    iqr = q3 - q1
    # calculate the lower bound of the IQR
    lower_bound = q1 -(1.5 * iqr) 
    # calculate the upper bound of the IQR
    upper_bound = q3 +(1.5 * iqr)
    for d in dataset:
        if(d < lower_bound):
            below_iqr.append(d)
        if(d > upper_bound):
            above_iqr.append(d)
        if(lower_bound <= d <= upper_bound):
            within_iqr.append(d)

    print(below_iqr)
    print(above_iqr)
    print(within_iqr)

if __name__ == "__main__":
    calculate_iqr()