import pandas as pd
import numpy as np
import xlrd
import openpyxl

xlsx = pd.ExcelFile('zadanie1\imiona.xlsx')
df = pd.read_excel(xlsx)
print(df[df['Liczba']>1000])
print("_________________________________")

print(df[df['Imie']=="WIKTORIA"])
print("_________________________________")

print(df.agg({'Liczba':['sum']}))
print("_________________________________")

przedzial = (df[((df.Rok>2000) & (df.Rok < 2005))])
print(przedzial.agg({'Liczba':['sum']}))
print("_________________________________")

chlopcy = (df[df['Plec']=="M"])
print(chlopcy.agg({'Liczba':['sum']}))
dziewczynki = (df[df['Plec']=="K"])
print(dziewczynki.agg({'Liczba':['sum']}))
print("_________________________________")

ilosc_imion = df.sort_values('Liczba', ascending=False).groupby(['Rok', 'Plec'])
for index, group in enumerate(ilosc_imion, start=1):
    print(f"{index} {group[0]}")
    print(f"{group[1].iloc[0]['Imie']}", end=' ')
    print(f"{group[1].iloc[0]['Liczba']}")
print("_________________________________")

dziewczynki = (df[((df.Plec=='K'))].sort_values(by="Liczba"))
chlopcy = (df[((df.Plec=='M'))].sort_values(by="Liczba"))
print(dziewczynki.tail(1))
print(chlopcy.tail(1))