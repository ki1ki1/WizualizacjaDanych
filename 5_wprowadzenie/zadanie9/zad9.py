def Parzyste(data):
    for i in range(len(data)):
        if i >= len(data):
            StopIteration
        else:
            if i%2==0:
                yield data[i]
def main():
    slowo = Parzyste("elektroencefalograf")
    for i in range(10):
        print(next(slowo))

if __name__ == "__main__":
    main()



    