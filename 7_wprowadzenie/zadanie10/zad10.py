import numpy as np
a = np.array([[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9]])
print(a)
b = a.reshape((27,3))
print(b)
#Możliwośći :81x1, 1x81, 27x3, 3x27, 9x9 - tylko te możliwości zapełnią całą macierz