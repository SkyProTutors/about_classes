class Cow:
    def __init__(self, name):
        self.name = name

    def sing(self):
        print(f"I am {self.name} and say Muuuuu")

class ColoredCow(Cow):
    def __init__(self, name, color):
        # super(ColoredCow, self).__init__(name)
        super().__init__(name)
        # Cow.__init__(self, name)
        self.color = color



class Bird:
    def fly(self):
        print("I can fly")


class Skliss(ColoredCow, Bird):
    pass


if __name__ == '__main__':
    cow1 = Cow("Burenka")
    cow1.sing()

    cow2 = ColoredCow("ALenke", "black")
    cow2.sing()
    print(cow2.color)

    sk = Skliss("Vasya", "white")
    sk.sing()
    sk.fly()

