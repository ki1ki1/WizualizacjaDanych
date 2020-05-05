import pandas as pd
import numpy as np
import xlrd
import openpyxl

xlsx = pd.ExcelFile('zadanie1\imiona.xlsx')
df = pd.read_excel(xlsx)
print(df.head())