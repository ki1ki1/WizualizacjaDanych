import numpy as np
def dodawanie(macierz, macierz2):
    a = np.sin(macierz)
    b = np.cos(macierz2)
    return a+b
macierz = np.array([[np.pi/2,np.pi/4,np.pi/3],[np.pi/6,5*np.pi/6,7*np.pi/6]])
macierz2 = np.array([[0, np.pi/4, np.pi/3],[np.pi/6, 5*np.pi/6, 7*np.pi/6]])
print( dodawanie(macierz,macierz2) )