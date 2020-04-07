class Robaczek:
    def __init__(self):
        self.x=0
        self.y=0
        self.krok=1
    def __del__(self):
        print('Obiekt został zniszczony')
    def idz_w_gore(self,ile_krokow):
        self.y += ile_krokow * self.krok
        return self.y 
    def idz_w_dol(self,ile_krokow):
        self.y -= ile_krokow * self.krok
        return self.y
    def idz_w_lewo(self,ile_krokow):
        self.x -= ile_krokow * self.krok
        return self.x
    def idz_w_prawo(self,ile_krokow):
        self.x += ile_krokow * self.krok
        return self.x
    def pokaz_gdzie_jestes(self):
        return self.x, self.y

def main():
    kroki = Robaczek()
    kroki.idz_w_gore(5)
    print(kroki.pokaz_gdzie_jestes())
    kroki.idz_w_dol(8)
    print(kroki.pokaz_gdzie_jestes())
    kroki.idz_w_lewo(8)
    print(kroki.pokaz_gdzie_jestes())
    kroki.idz_w_prawo(8)
    print(kroki.pokaz_gdzie_jestes())
    kroki.idz_w_gore(1)
    print(kroki.pokaz_gdzie_jestes())
    del kroki
    kroki.idz_w_lewo(3)
    print(kroki.pokaz_gdzie_jestes())
if __name__ == "__main__":
    main()