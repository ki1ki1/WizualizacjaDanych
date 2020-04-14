import itertools 
liczby=[1,2,3,4,5,6,7,8,9,10]
x = itertools.combinations(liczby, 3)

for i in range(10):
    print(next(x))