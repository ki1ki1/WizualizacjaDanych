lista = []
for x in range(0,40,4):
    lista += [x]
plik=open("dane.txt","a+")
plik.writelines(str(lista))
plik.close()