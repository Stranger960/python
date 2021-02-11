from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, v):
        self.v = v

    @abstractmethod
    def calc(self):
        pass


class Coat(Clothes):
    def __init__(self, w):
        self.w = w
        Clothes.__init__(self, w)

    @property
    def calc(self):
        c = (self.w / 6.5 + 0.5)
        Clothes.calc(self)

        return c


class Suit(Clothes):
    def __init__(self, h):
        self.h = h
        Clothes.__init__(self, h)

    @property
    def calc(self):
        s = (2 * self.h + 0.3)
        Clothes.calc(self)
        return s


My_Suit = Suit(50)
My_Coat = Coat(52)

print(f'\nResult for coat: {My_Coat.calc}\nResult for suit: {My_Suit.calc}')
print(f'\nTotal result: {My_Coat.calc + My_Suit.calc}')