class Samogloski:
    def __init__(self, data):
        self.data = data
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if(isinstance(self.data, str)):
            if self.index >= len(self.data):
                raise StopIteration
            samogloski = ["a","e","i","o","u","y"]
            for i in range(len(samogloski)):
                if samogloski[i] == self.data[self.index]:
                    print(self.data[self.index])
            self.index += 1
        else:
            print("Podany ciag nie jest słowem :)")
def main():
    for i in Samogloski("elektroencefalograf"):
        i

    
if __name__ == "__main__":
    main()