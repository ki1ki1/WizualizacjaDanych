import numpy as np
import pandas as pd
import xlrd
import openpyxl
import matplotlib.pyplot as plt

xlsx = pd.ExcelFile('zadanie1/imiona.xlsx')
df = pd.read_excel(xlsx)

x = df.groupby(["Rok"]).agg({"Liczba": ['count']})
wykres = x.plot()
wykres.set_ylabel('Rok')
wykres.set_xlabel('Liczba')
wykres.legend()
plt.title('Liczba urodzonych dzieci w danym roku')
plt.show()