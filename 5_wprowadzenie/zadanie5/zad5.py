class Osoba:

    def __init__(self, imie, nazwisko):
        self.imie = imie
        self.nazwisko = nazwisko

    def przedstaw_sie(self):
        return "{} {}".format(self.imie, self.nazwisko)

class Pracownik(Osoba):

    def __init__(self, imie, nazwisko, pensja):
        Osoba.__init__(self, imie, nazwisko)
        # lub
        # super().__init__(imie, nazwisko)
        self.pensja = pensja

    def przedstaw_sie(self):
        return "{} {} i zarabiam {}".format(self.imie, self.nazwisko, self.pensja)

class Menadzer(Pracownik):

    def przedstaw_sie(self):
        return "{} {}, jestem menadżerem i zarabiam {}".format(self.imie, self.nazwisko, self.pensja)


jozek = Pracownik("Józek", "Bajka", 2000)
adrian = Menadzer("Adrian", "Mikulski", 12000)
julek = Osoba("Julek", "Miłosiński")

print(jozek.przedstaw_sie())
print(adrian.przedstaw_sie())
print(julek.przedstaw_sie())

print(isinstance(jozek, Osoba))
print(isinstance(adrian, Osoba))
print(isinstance(jozek, Menadzer))
print(isinstance(adrian, Menadzer))
print(isinstance(jozek, Pracownik))
print(isinstance(adrian, Pracownik))
print(isinstance(julek, Osoba))
print(isinstance(julek, Menadzer))
print(isinstance(julek, Pracownik))

print(issubclass(Pracownik,Osoba))
print(issubclass(Menadzer,Osoba))
print(issubclass(Osoba,Pracownik))
print(issubclass(Menadzer,Pracownik))