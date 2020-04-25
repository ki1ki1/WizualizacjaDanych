import numpy as np
a = np.array( [[20,30,40],[20,30,40],[20,30,40]] )
b = np.array( [[20,30,40],[20,30,40],[20,30,40],[20,30,40]] )
print(a.min(axis=1))
print(b.min(axis=1))
print(a.max(axis=1))
print(b.max(axis=1))
