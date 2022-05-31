import numpy as np
import itertools
import math
from numpy import genfromtxt
from itertools import combinations
from math import hypot
# Currently, the user has to pre-format their xy data output as a 2-column csv.
raw_data = genfromtxt('~path/testdata.csv', delimiter=',')
# Convert from csv into a python-readable data array. Print it out to confirm.
coords = np.array(raw_data)
# Define each xy pair as a point, and find the distance between each point and every other point (n choose 2)
def distance(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return hypot(x2 - x1, y2 - y1)
dist = [distance(*combo) for combo in combinations(coords, 2)]
#Simply sums all the inter-individual distance, then takes the arithmetic mean
len(dist)
result = np.mean(dist)
# Output to csv
import pandas as pd
dict={'result', result}
df = pd.DataFrame(dict)
df.to_csv('~path/output.csv')
