##JH Daten einlesen und aufbereiten

import pandas as pd
import os
from pathlib import Path
import numpy as np
#import pyreadstat

p = Path.cwd()
print(p)
# /Users/mbp/Documents/my-project/python-snippets/notebook

print(type(p))


os.getcwd()


# data = pd.read_csv('..\data/iris.csv',sep=',',header=0)
#data=pd.read_excel("C:/Users/jhardt/Documents/PYTHON/Data/Census-Datensatz.xlsx")



#data_iris = pd.read_csv('data/iris.csv',sep=',',header=0)
#data_iris.head()
