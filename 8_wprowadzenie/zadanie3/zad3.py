import numpy as np 
import pandas as pd

df = pd.read_csv('zadanie3/zamowienia.csv',sep=";")
print("_________________________________")

print(df["Sprzedawca"].unique())
print("_________________________________")

print(df.sort_values(by="Utarg").tail(5))
print("_________________________________")

print(df.groupby(["Sprzedawca"]).agg({"idZamowienia":['count']}))
print("_________________________________")

print(df.groupby(["Kraj"]).agg({"idZamowienia":['count']}))
print("_________________________________")

suma=(df[((df.Kraj == "Polska") & (df.DataZamowienia>"2004-12-31") & (df.DataZamowienia<"2006-01-01"))].agg({"idZamowienia":['count']}))
print(suma)
print("_________________________________")

sredni=(df[((df.DataZamowienia>"2003-12-31") & (df.DataZamowienia<"2005-01-01"))].agg({"Utarg":['average']}))
print(sredni)
print("_________________________________")

plik2 = open("zadanie3/zamowienia_2004.csv","w+")
plik2.write(str(sredni))
plik2.close()
plik = open("zadanie3/zamowienia_2005.csv","w+")
plik.write(str(suma))
plik.close()