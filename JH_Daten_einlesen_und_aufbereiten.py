##JH Daten einlesen und aufbereiten

import pandas as pd
import os
from pathlib import Path
import numpy as np
#import pyreadstat

data_iris = pd.read_csv('data/iris.csv',sep=',',header=0)
data_iris.head()

data_census = pd.read_csv('data/census.csv',sep=',',header=0)
data_census.head()



#os.getcwd()

# data = pd.read_csv('..\data/iris.csv',sep=',',header=0)
#data=pd.read_excel("C:/Users/jhardt/Documents/PYTHON/Data/Census-Datensatz.xlsx")
# data = open(r"C:\Users\jhardt\Documents\PYTHON\Data\Census-Datensatz.xlsx")
# Pfad klappt, aber Permission Error (evtl. wg. fehlendem Admin-Account)
#Census-Datensatz.xlsx

#data_iris = pd.read_csv('data/iris.csv',sep=',',header=0)
#data_iris.head()

# Befehle für Modul pathlib
# p = Path.cwd()
# print(p)
# /Users/mbp/Documents/my-project/python-snippets/notebook

# print(type(p))