import numpy as np 
def przekatna(n):
    przekatna=[]
    for i in range(n):
        przekatna.append(2)            
    A = np.diag(przekatna) 
    for a in range(0,n):
        for b in range(0,n):
            for c in range(1,n+1):
                if(a==b+c or b==a+c):  
                    A[a,b]=2*(c+1)    
    return A                
        
print(przekatna(8))