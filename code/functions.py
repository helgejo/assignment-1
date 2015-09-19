from __future__ import division
import csv
import copy
from id3 import *
from eval import *
import functions
import numpy as np
import matplotlib.pyplot as plt


__author__ = 'Helge'


def load_adult_data(filename):
    records = []
    with open(filename, 'rb') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        for row in csvreader:
            if len(row) == 15:  # if we have all fields in that line
                records.append({
                    "age": int(row[0].strip()),
                    "workclass": row[1].strip(),
                    "fnlwgt": int(row[2].strip()),
                    "education": row[3].strip(),
                    "education-num": int(row[4].strip()),
                    "marital-status": row[5].strip(),
                    "occupation": row[6].strip(),
                    "relationship": row[7].strip(),
                    "race": row[8].strip(),
                    "sex": row[9].strip(),
                    "capital-gain": int(row[10].strip()),
                    "capital-loss": int(row[11].strip()),
                    "hours-per-week": int(row[12].strip()),
                    "native-country": row[13].strip(),
                    "class": row[14].strip()
                })
            elif len(row) == 14:  # if we have all fields in that line
                records.append({
                    "age": int(row[0].strip()),
                    "workclass": row[1].strip(),
                    "fnlwgt": int(row[2].strip()), # Remove
                    "education": row[3].strip(),
                    "education-num": int(row[4].strip()), # Remove
                    "marital-status": row[5].strip(), # Remove
                    "occupation": row[6].strip(),
                    "relationship": row[7].strip(),
                    "race": row[8].strip(),
                    "sex": row[9].strip(),
                    "capital-gain": int(row[10].strip()),
                    "capital-loss": int(row[11].strip()),
                    "hours-per-week": int(row[12].strip()),
                    "native-country": row[13].strip(), # Remove
                })
    return records

def removeCont(adult):
    for row in adult:
        del row["age"]
        del row["fnlwgt"]
        del row["education-num"]
        del row["capital-gain"]
        del row["capital-loss"]
        del row["hours-per-week"]

def preProcess(adult):
    for row in adult:
        del row["native-country"]
        del row["fnlwgt"]
        del row["education-num"]
        del row["marital-status"]

def descritize(adult):

    #handle age (max:90, min: 17)
    ageBin = np.linspace(15.0, 91.0, num=11)

    # handle capital-gain (Max: 99999, min 0 )
    CapGBin = np.linspace(0.0, 100000.0, num=1500)

    #handle capital-loss (4356, 0)
    CapLBin = np.linspace(0.0, 4400.0, num=500)

    #handle hours-per-week (99, 1)
    Hbin = np.linspace(0.0, 100.0, num=2)

    age = descr(adult, "age", ageBin)
    CapG = descr(adult, "capital-gain", CapGBin)
    CapL = descr(adult, "capital-loss", CapLBin)
    hpw = descr(adult, "hours-per-week", Hbin)

def descr(data, col, bins):
    dic = {}
    values = np.array([record[col] for record in data])
    inds = np.digitize(values, bins)
    for i in range(values.size):
        dic[values[i]] = str(bins[inds[i]])

    for row in data:
        row[col] = dic[row[col]]
    return dic


def splitData(data, mod):
    for i in range(len(data)):
        if mod == -1:
            train.append(data[i])
        elif i % mod == 0:  # test instance
            test.append(data[i])
        else:  # train instance
            train.append(data[i])


train = []  # list to be filled with training data
test = []  # list to be filled with test data
adult_data = load_adult_data("../data/adult.minidata")
preProcess(adult_data)
descritize(adult_data)
print adult_data

#print adult_data[0]["age"]