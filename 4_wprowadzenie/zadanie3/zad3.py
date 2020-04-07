lista = ["Puma","Lew","Tygrys","Jamnik"]
with open("dane.txt", "w") as plik:
    plik.writelines(str(lista))
with open("dane.txt", "r") as plik:
    wiersze = plik.readlines()
print(wiersze)