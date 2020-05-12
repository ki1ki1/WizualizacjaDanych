import numpy as np
import pandas as pd
import xlrd
import openpyxl
import matplotlib.pyplot as plt

xlsx = pd.ExcelFile('zadanie3/imiona.xlsx')
df = pd.read_excel(xlsx)


x =(df[((df.Rok > 2012) & ( df.Rok< 2018))].groupby(['Plec']).agg({'Liczba': ['sum']}))
wykres = x.plot.pie(subplots=True,autopct='%.1f %%', fontsize=20, figsize=(6, 6))
plt.title("Suma urodzonych dzieci w latach 2013-2017 z podziałem na płeć")
plt.show()