##JH Daten einlesen und aufbereiten

from pathlib import Path
# import os
import openpyxl

import pandas as pd
import numpy as np
import pyreadstat as stat

# data_iris = pd.read_csv('data/iris.csv',sep=',',header=0)
# data_iris.head()

# data_census = pd.read_csv('data/census.csv',sep=',',header=0)
# data_census.head()

# Befehle für Modul pathlib
# p = Path.cwd()
# print(p)
#/Users/mbp/Documents/my-project/python-snippets/notebook

# path = Path('/etc')
# os.chdir(path)

# path = Path(r"C:\Users\jhardt\Documents\PYTHON\Dig_DS_Projektarbeit\")
# os.chdir(path)


#os.getcwd()

# data = pd.read_csv('..\data/iris.csv',sep=',',header=0)

# data=pd.read_excel("C:/Users/jhardt/Documents/PYTHON/Data/Census-Datensatz.xlsx")
# data=pd.read_excel(r "C:/Users/jhardt/Documents/PYTHON/Data/Census-Datensatz.xlsx")

# data_test=pd.read_excel("C:/Users/jhardt/Documents/PYTHON/Data/Test.xlsx")
# print(data_test)
# funktioniert

# data=pd.read_excel(r"C:/Users/jhardt/Documents/PYTHON/Data/Test.xlsx")
# scheint durchzulaufen (Pfad erscheint), aber unklar, ob und wo Daten eingelesen wurden

# data_test=pd.read_excel(r"C:\Users\jhardt\Documents\PYTHON\Data\Test.xlsx")
# print(data_test)
# funktioniert

# data_test = open(r"C:\Users\jhardt\Documents\PYTHON\Data\Test.xlsx")
# print(data_test)
# unklar, wie es funktioniert
# Meldung: <_io.TextIOWrapper name='C:\\Users\\jhardt\\Documents\\PYTHON\\Data\\Test.xlsx' mode='r' encoding='cp1252'>

# Pfad klappt, aber Permission Error (evtl. wg. fehlendem Admin-Account)
#Census-Datensatz.xlsx

#data_iris = pd.read_csv('data/iris.csv',sep=',',header=0)
#data_iris.head()

# print(type(p))

# Commands from openpyxl==3.1.2
# Save the file
# wb.save("sample.xlsx")
