def Miesiace():
    Miesiace = ["Styczeń","Luty","Marzec","Kwiecień","Maj","Czerwiec","Lipiec","Sierpień","Wrzesień","Październik","Listopad","Grudzień"]
    for i in Miesiace:
        yield i
def main():
    months = Miesiace()
    for i in range(12):
        print(next(months))
if __name__ == "__main__":
    main()