import numpy as np 
def fibbonacci(n):
    result = [1,1]
    for i in range(n-2):
        result.append(result[i] + result[(i + 1)])
    a = np.array([[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]])
    i = 0
    k = 0
    l = 0
    while i < n:
        if l==5:
            k+=1
            l=0
        a[k][l] = result[i]
        i+=1
        l+=1
        
    return a
print(fibbonacci(25))