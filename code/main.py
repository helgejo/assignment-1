from __future__ import division
import csv
import copy
import id3
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
    return records


adult_data = load_adult_data("../data/adult.minidata")
noncat_data = copy.deepcopy(adult_data)
for row in noncat_data:
    del row["age"]
    del row["fnlwgt"]
    del row["education-num"]
    del row["capital-gain"]
    del row["capital-loss"]
    del row["hours-per-week"]

#print adult_data[0]
#print noncat_data[0]

train = []  # train
test = []  # test

for i in range(len(noncat_data)):
    if i % 3 == 0:  # test instance
        test.append(noncat_data[i])
    else:  # train instance
        train.append(noncat_data[i])

attributes = train[0].keys()


def create_decision_tree(data, attributes, target_attr):
    # copy the dataset
    data = data[:]
    # list of target values in dataset
    vals = [record[target_attr] for record in data]

    def unique(seq):
        # Method to find unique values in list
        seen = set()
        seen_add = seen.add
        return [ x for x in seq if not (x in seen or seen_add(x))]

    def count(vals):
        # Count instances of value in list
        hig_val = 0
        res = ""
        instances = unique(vals)
        for val in instances:
            z = 0
            for row in data:
                z += sum( x == val for x in row.values() )
            if z >= hig_val:
                res = val
                hig_val = z
        return res


    def choose_attribute(data, attributes, target_attr):
        #Find the attribute with the highest gain
        data = data[:]
        best_gain = 0.0
        best_attr = None

        for attr in attributes:
            # TODO test gain function
            gain = gain(data, attr, target_attr)
            if (gain >= best_gain and attr != target_attr):
                best_gain = gain
                best_attr = attr

        return best_attr

    default = count(vals)

     # If training or attribute set is empty, return default;
    if not data or (len(attributes) - 1) <= 0:
            return default

    # If S consists of records all with the same value for
	#the categorical attribute, return default;
    elif vals.count(vals[0]) == len(vals):
        return vals[0]

        # Let D be the attribute with largest Gain(D,S)
	#    among attributes in set of attributes;
	# Let {dj| j=1,2, .., m} be the values of attribute D;
	# Let {Sj| j=1,2, .., m} be the subsets of S consisting
	#    respectively of records with value dj for attribute D;
	# Return a tree with root labeled D and arcs labeled
	#    d1, d2, .., dm going respectively to the trees
    #
	#      ID3(R-{D}, C, S1), ID3(R-{D}, C, S2), .., ID3(R-{D}, C, Sm);
    else:
        # Choose the next best attribute to best classify our data
        best = choose_attribute(data, attributes, target_attr)
        print best
        # Create a new decision tree/node with the best attribute and an empty
        # dictionary object
        tree = {best:{}}
        print tree

    #return tree

create_decision_tree(train, attributes, "class")