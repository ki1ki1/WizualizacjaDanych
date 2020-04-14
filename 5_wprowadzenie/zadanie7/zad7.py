class Parzyste:
    def __init__(self, data):
        self.data = data
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.data):
            raise StopIteration
        if self.index%2==0:
            print(self.data[self.index])
        else:
            print(" ")
        self.index += 1
def main():
    for i in Parzyste("elektroencefalograf"):
        i

if __name__ == "__main__":
    main()