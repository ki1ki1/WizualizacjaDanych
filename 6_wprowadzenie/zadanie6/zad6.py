import numpy as np 
slowa = ['tarcin','aehqke','beczka','ewezwe','lasaka','axcuia']
s =[[],[],[],[],[],[]]
for i in range(0,6,1):
    s[i] = np.array(list(slowa[i]))
    s[i] = np.fromiter(slowa[i], dtype='U1')
    print(s[i])

#pierwsza kolumna, głowna przekatna, piąty wiersz, trzeci wiersz
