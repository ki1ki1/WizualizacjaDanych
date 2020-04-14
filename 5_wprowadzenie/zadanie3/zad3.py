class Kwadrat():
    def __init__(self, x):
        self.x =x
        self.y=x
    def __gt__(self,bok):
        return self.x > bok.x
    def __ge__(self,bok):
        return self.x >= bok.x
    def __le__(self,bok):
        return self.x <= bok.x
    def __lt__(self,bok):
        return self.x < bok.x
def main():
    kwadrat = Kwadrat(12)
    kwadrat2 = Kwadrat(16)

    print(kwadrat>kwadrat2)
    print(kwadrat>=kwadrat2)
    print(kwadrat<=kwadrat2)
    print(kwadrat<kwadrat2)
    if kwadrat>=kwadrat2:
        print("Dobrze!")
    else:
        print("Źle!")

if __name__ == "__main__":
    main()
    
    
