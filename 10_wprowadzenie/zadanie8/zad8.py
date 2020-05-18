import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def kostka(n):
    return [(np.random.randint(6)+1)+(np.random.randint(6)+1) for x in range(n)]

lista=kostka(50)
print(lista)
plt.hist(lista, bins=10, facecolor="red", alpha=0.75)
plt.xlabel('Wartości')
plt.ylabel('Rzuty')
plt.grid(True)
plt.show()