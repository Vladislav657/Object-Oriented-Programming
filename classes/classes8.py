class Track:
    def __init__(self, start_x=0, start_y=0):
        self.start_x = start_x
        self.start_y = start_y
        self.lines = [TrackLine(start_x, start_y, None)]

    def add_track(self, tr):
        self.lines.append(tr)

    def get_tracks(self):
        return tuple(self.lines)

    @staticmethod
    def get_len(lines):
        return sum([((lines[i].to_x - lines[i - 1].to_x) ** 2 + (lines[i].to_y - lines[i - 1].to_y) ** 2) ** 0.5 for i
                    in range(1, len(lines))])

    def __eq__(self, other):
        return self.get_len(self.lines) == self.get_len(other.lines)

    def __lt__(self, other):
        return self.get_len(self.lines) < self.get_len(other.lines)

    def __len__(self):
        return int(self.get_len(self.lines))


class TrackLine:
    def __init__(self, to_x, to_y, max_speed):
        self.to_x = to_x
        self.to_y = to_y
        self.max_speed = max_speed


class Dimensions:
    MIN_DIMENSION = 10
    MAX_DIMENSION = 10000

    def __init__(self, a, b, c):
        self.__a = a
        self.__b = b
        self.__c = c

    def get_a(self):
        return self.__a

    def set_a(self, a):
        if self.MIN_DIMENSION <= a <= self.MAX_DIMENSION:
            self.__a = a

    def get_b(self):
        return self.__b

    def set_b(self, b):
        if self.MIN_DIMENSION <= b <= self.MAX_DIMENSION:
            self.__b = b

    def get_c(self):
        return self.__c

    def set_c(self, c):
        if self.MIN_DIMENSION <= c <= self.MAX_DIMENSION:
            self.__c = c

    a = property(get_a, set_a)
    b = property(get_b, set_b)
    c = property(get_c, set_c)

    @staticmethod
    def get_volume(dim):
        return dim.a * dim.b * dim.c

    def __lt__(self, other):
        return self.get_volume(self) < self.get_volume(other)

    def __le__(self, other):
        return self.get_volume(self) <= self.get_volume(other)


class ShopItem:
    def __init__(self, name, price, dim):
        self.name = name
        self.price = price
        self.dim = dim


class StringText:
    def __init__(self, lst_words):
        self.lst_words = lst_words

    def __lt__(self, other):
        return len(self.lst_words) < len(other.lst_words)

    def __le__(self, other):
        return len(self.lst_words) <= len(other.lst_words)


class Morph:
    def __init__(self, *args):
        self.words = [i.lower() for i in args]

    def add_word(self, word):
        if word not in self.words:
            self.words.append(word.lower())

    def get_words(self):
        return tuple(self.words)

    def __eq__(self, other):
        if type(other) == Morph:
            return self in other.words
        else:
            return other.lower() in self.words


class FileAcceptor:
    def __init__(self, *args):
        self.extensions = list(args)

    def __call__(self, *args, **kwargs):
        for i in self.extensions:
            if args[0].endswith(f'.{i}'):
                return True
        return False

    def __add__(self, other):
        return FileAcceptor(*set([i for i in self.extensions + other.extensions]))


class MoneyR:
    def __init__(self, volume=0):
        self.__volume = volume
        self.__cb = None

    def get_volume(self):
        return self.__volume

    def set_volume(self, volume):
        self.__volume = volume

    def get_cb(self):
        return self.__cb

    def set_cb(self, cb):
        self.__cb = cb

    def __get_rates(self):
        if self.cb is None:
            raise ValueError("Неизвестен курс валют.")
        return {MoneyE: self.cb.rates['euro'], MoneyD: self.cb.rates['dollar'], MoneyR: self.cb.rates['rub']}

    def __eq__(self, other):
        rates = self.__get_rates()
        return round(self.volume / rates[type(self)], 1) == round(other.volume / rates[type(other)], 1)

    def __le__(self, other):
        rates = self.__get_rates()
        return round(self.volume / rates[type(self)], 1) <= round(other.volume / rates[type(other)], 1)

    def __lt__(self, other):
        rates = self.__get_rates()
        return round(self.volume / rates[type(self)], 1) < round(other.volume / rates[type(other)], 1)

    volume = property(get_volume, set_volume)
    cb = property(get_cb, set_cb)


class MoneyD:
    def __init__(self, volume=0):
        self.__volume = volume
        self.__cb = None

    def get_volume(self):
        return self.__volume

    def set_volume(self, volume):
        self.__volume = volume

    def get_cb(self):
        return self.__cb

    def set_cb(self, cb):
        self.__cb = cb

    def __get_rates(self):
        if self.cb is None:
            raise ValueError("Неизвестен курс валют.")
        return {MoneyE: self.cb.rates['euro'], MoneyD: self.cb.rates['dollar'], MoneyR: self.cb.rates['rub']}

    def __eq__(self, other):
        rates = self.__get_rates()
        return round(self.volume / rates[type(self)], 1) == round(other.volume / rates[type(other)], 1)

    def __le__(self, other):
        rates = self.__get_rates()
        return round(self.volume / rates[type(self)], 1) <= round(other.volume / rates[type(other)], 1)

    def __lt__(self, other):
        rates = self.__get_rates()
        return round(self.volume / rates[type(self)], 1) < round(other.volume / rates[type(other)], 1)

    volume = property(get_volume, set_volume)
    cb = property(get_cb, set_cb)


class MoneyE:
    def __init__(self, volume=0):
        self.__volume = volume
        self.__cb = None

    def get_volume(self):
        return self.__volume

    def set_volume(self, volume):
        self.__volume = volume

    def get_cb(self):
        return self.__cb

    def set_cb(self, cb):
        self.__cb = cb

    def __get_rates(self):
        if self.cb is None:
            raise ValueError("Неизвестен курс валют.")
        return {MoneyE: self.cb.rates['euro'], MoneyD: self.cb.rates['dollar'], MoneyR: self.cb.rates['rub']}

    def __eq__(self, other):
        rates = self.__get_rates()
        return round(self.volume / rates[type(self)], 1) == round(other.volume / rates[type(other)], 1)

    def __le__(self, other):
        rates = self.__get_rates()
        return round(self.volume / rates[type(self)], 1) <= round(other.volume / rates[type(other)], 1)

    def __lt__(self, other):
        rates = self.__get_rates()
        return round(self.volume / rates[type(self)], 1) < round(other.volume / rates[type(other)], 1)

    volume = property(get_volume, set_volume)
    cb = property(get_cb, set_cb)


class CentralBank:
    rates = {'rub': 72.5, 'dollar': 1.0, 'euro': 1.15}

    def __new__(cls, *args, **kwargs):
        return None

    @classmethod
    def register(cls, money):
        money.cb = cls


class Body:
    def __init__(self, name, ro, volume):
        self.name = name
        self.ro = ro
        self.volume = volume

    def __eq__(self, other):
        bd = other if type(other) in (int, float) else other.ro * other.volume
        return self.ro * self.volume == bd

    def __lt__(self, other):
        bd = other if type(other) in (int, float) else other.ro * other.volume
        return self.ro * self.volume < bd


class Box:
    def __init__(self):
        self.box = []

    def add_thing(self, obj):
        self.box.append(obj)

    def get_things(self):
        return self.box

    def __eq__(self, other):
        for i in self.box:
            if i not in other.box:
                return False
        return True


class Thing:
    def __init__(self, name, mass):
        self.name = name
        self.mass = mass

    def __eq__(self, other):
        return self.name.lower() == other.name.lower() and self.mass == other.mass
