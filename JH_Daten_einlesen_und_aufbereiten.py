##JH Daten einlesen und aufbereiten

import pandas as pd
import os
import numpy as np

data_iris = pd.read_csv('data/iris.csv',sep=',',header=0)
data_iris.head()
