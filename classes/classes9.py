class Rect:
    def __init__(self, x, y, width, height):
        self.x, self.y = x, y
        self.width, self.height = width, height

    def __hash__(self):
        return hash((self.width, self.height))


class ShopItem:
    def __init__(self, name, weight, price):
        self.name = name
        self.weight = weight
        self.price = price

    def __hash__(self):
        return hash((self.name.lower(), self.weight, self.price))

    def __eq__(self, other):
        return hash(self) == hash(other)


class DataBase:
    def __init__(self, path=''):
        self.path = path
        self.dict_db = {}

    def write(self, record):
        if record not in self.dict_db:
            self.dict_db[record] = [record]
        else:
            self.dict_db[record].append(record)

    def read(self, pk):
        for key in self.dict_db:
            for elem in self.dict_db[key]:
                if elem.pk == pk:
                    return elem


class Record:
    pk = 0

    def __init__(self, fio, descr, old):
        self.pk = Record.pk
        self.fio = fio
        self.descr = descr
        self.old = old
        Record.pk += 1

    def __hash__(self):
        return hash((self.fio.lower(), self.old))

    def __eq__(self, other):
        return hash(self) == hash(other)


class BookStudy:
    def __init__(self, name, author, year):
        self.name = name
        self.author = author
        self.year = year

    def __hash__(self):
        return hash((self.name.lower(), self.author.lower()))


class Dimensions:
    def __init__(self, a, b, c):
        if a <= 0 or b <= 0 or c <= 0:
            raise ValueError("габаритные размеры должны быть положительными числами")
        self.a, self.b, self.c = a, b, c

    def __hash__(self):
        return hash((self.a, self.b, self.c))


class NumberValue:
    def __set_name__(self, owner, name):
        self.name = '__' + name

    def __get__(self, instance, value):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        if type(value) not in (int, float) or value <= 0:
            raise ValueError("длины сторон треугольника должны быть положительными числами")
        setattr(instance, self.name, value)


class Triangle:
    a = NumberValue()
    b = NumberValue()
    c = NumberValue()

    def __init__(self, a, b, c):
        if a < b + c and b < a + c and c < a + b:
            self.a, self.b, self.c = a, b, c
        else:
            raise ValueError("с указанными длинами нельзя образовать треугольник")

    def __len__(self):
        return int(self.a + self.b + self.c)

    def __call__(self, *args, **kwargs):
        p = (self.a + self.b + self.c) / 2
        return (p * (p - self.a) * (p - self.b) * (p - self.c)) ** 0.5
