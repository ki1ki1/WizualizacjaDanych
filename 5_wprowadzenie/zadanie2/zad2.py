class Kwadrat():
    def __init__(self, x):
        self.x =x
        self.y=x
    def __add__(self,bok):
        wynik = self.x+bok.x
        return wynik
def main():
    kwadrat1 = Kwadrat(12)
    kwadrat2=Kwadrat(18)
    kwadrat3= kwadrat1+kwadrat2
    print(kwadrat3)
if __name__ == "__main__":
    main()
    
    
