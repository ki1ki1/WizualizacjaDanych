import numpy as np
import pandas as pd
import xlrd
import openpyxl
import matplotlib.pyplot as plt

xlsx = pd.ExcelFile('zadanie2/imiona.xlsx')
df = pd.read_excel(xlsx)

l = df.groupby(['Plec']).agg({"Liczba": ['sum']})
wykres = l.plot.bar()
wykres.legend()
wykres.set_ylabel('Mln')
wykres.set_xlabel('Płeć')
plt.title('Suma urodzonych dzieci w latach 2000-2017 z podziałem na płeć')

plt.show()