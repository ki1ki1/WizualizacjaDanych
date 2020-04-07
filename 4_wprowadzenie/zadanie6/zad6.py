class Slowa:
    def __init__(self,slowo1,slowo2):
        self.slowo1=slowo1
        self.slowo2=slowo2
    def czy_palindrom(self): 
        odtylu = self.slowo1[::-1] 
        if (self.slowo1 == odtylu): 
            return "słowo jest palindromem"
        return "słowo nie jest palindromem"
    def czy_metagramy(self):
        wynik = 0
        if self.slowo1 != self.slowo2:
            if len(self.slowo1) == len(self.slowo2):
                for i in range(len(self.slowo1)):
                    for j in range(len(self.slowo2)):
                        if self.slowo1[i] != self.slowo2[j]:
                            wynik+=1
                        i+=1
                    if i>=len(self.slowo2):
                        break
                if wynik>1:
                    return "słowa nie sa metagramami"
                return "słowa sa metagramami"
            return "słowa maja inna dlugosc"
        return "słowa są takie same, nie mogą być metagramami"
    def czy_anagramy(self):
        if(sorted(self.slowo1)==sorted(self.slowo2)):
            return "slowa sa anagramami"
        return "slowa nie sa anagramami"
def main():
    wyrazy = Slowa("kasa","owca")
    print(wyrazy.czy_palindrom())
    print(wyrazy.czy_metagramy())
    print(wyrazy.czy_anagramy())
if __name__ == "__main__":
    main()