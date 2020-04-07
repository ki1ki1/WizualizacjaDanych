class Ciagi:
    def __init__(self):
        self.a1=0
        self.a2=0
        self.a3=0
        self.a4=0
        self.a5=0
    def wyswietl_dane(self):
        return self.a1,self.a2,self.a3,self.a4,self.a5
    def pobierz_elementy(self,a1,a2,a3,a4,a5):
        self.a1=a1
        self.a2=a2
        self.a3=a3
        self.a4=a4
        self.a5=a5
        return self.a1,self.a2,self.a3,self.a4,self.a5
    def pobierz_parametry(self,pierw,r,n):
        self.pierw=pierw
        self.r=r
        self.n=n
        return self.pierw,self.r,self.n
    def policz_sume(self):
        wynik = ((2*self.pierw+(self.n-1)*self.r)/2)*self.n
        return wynik
    def policz_elementy(self):
        wynik = 0
        if(self.pierw==self.n):
            return 1
        for i in range(self.pierw,self.n,self.r):
            wynik+=1
        return wynik
def main():
    ciag = Ciagi()
    print(ciag.wyswietl_dane())
    print(ciag.pobierz_elementy(1,2,3,4,5))
    ciag.pobierz_parametry(1,2,6)
    print(ciag.policz_sume())
    print(ciag.policz_elementy())
if __name__ == "__main__":
    main()