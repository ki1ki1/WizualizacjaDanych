class NaZakupy:
    def __init__(self,nazwa_produktu,ilosc,jednostka_miary, cena_jed):
        self.nazwa_produktu=nazwa_produktu
        self.ilosc=ilosc
        self.jednostka_miary=jednostka_miary
        self.cena_jed=cena_jed
    def wyswietl_produkt(self):
        return self.nazwa_produktu,self.ilosc,self.jednostka_miary,self.cena_jed
    def ile_produktu(self):
        ile = self.ilosc * 1
        return ile, self.jednostka_miary
    def ile_kosztuje(self):
        ile = self.ilosc * self.cena_jed
        return ile
def main():
    Plyn = NaZakupy("Płyn do dezynfekcji",100,"L",1000)
    print(Plyn.wyswietl_produkt())
    print(Plyn.ile_produktu())
    print(Plyn.ile_kosztuje())
if __name__ == "__main__":
    main()