class Book:
    def __init__(self, title, author, pages, year):
        self.title = title
        self.author = author
        self.pages = pages
        self.year = year


class DigitBook(Book):
    def __init__(self, title, author, pages, year, size, frm):
        super(DigitBook, self).__init__(title, author, pages, year)
        self.size = size
        self.frm = frm


class Thing:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight


class ArtObject(Thing):
    def __init__(self, name, weight, author, date):
        super(ArtObject, self).__init__(name, weight)
        self.author = author
        self.date = date


class Computer(Thing):
    def __init__(self, name, weight, memory, cpu):
        super(Computer, self).__init__(name, weight)
        self.memory = memory
        self.cpu = cpu


class Auto(Thing):
    def __init__(self, name, weight, dims):
        super(Auto, self).__init__(name, weight)
        self.dims = dims


class Mercedes(Auto):
    def __init__(self, name, weight, dims, model, old):
        super(Mercedes, self).__init__(name, weight, dims)
        self.model = model
        self.old = old


class Toyota(Auto):
    def __init__(self, name, weight, dims, model, wheel):
        super(Toyota, self).__init__(name, weight, dims)
        self.model = model
        self.wheel = wheel


class SellItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class House(SellItem):
    def __init__(self, name, price, material, square):
        super(House, self).__init__(name, price)
        self.material = material
        self.square = square


class Flat(SellItem):
    def __init__(self, name, price, size, rooms):
        super(Flat, self).__init__(name, price)
        self.size = size
        self.rooms = rooms


class Land(SellItem):
    def __init__(self, name, price, square):
        super(Land, self).__init__(name, price)
        self.square = square


class Agency:
    def __init__(self, name):
        self.name = name
        self.items = []

    def add_object(self, obj):
        self.items.append(obj)

    def remove_object(self, obj):
        self.items.remove(obj)

    def get_objects(self):
        return self.items


class Router:
    app = {}

    @classmethod
    def get(cls, path):
        return cls.app.get(path)

    @classmethod
    def add_callback(cls, path, func):
        cls.app[path] = func


class Callback:
    def __init__(self, path, route_cls):
        self.path = path
        self.route_cls = route_cls

    def __call__(self, *args, **kwargs):
        self.route_cls.add_callback(self.path, args[0])


def integer_params_decorated(func):
    def wrapper(self, *args, **kwargs):
        if not all(type(i) == int for i in args) or not all(type(j) == int for j in kwargs.values()):
            raise TypeError("аргументы должны быть целыми числами")
        return func(self, *args, **kwargs)
    return wrapper


def integer_params(cls):
    methods = {k: v for k, v in cls.__dict__.items() if callable(v)}
    for k, v in methods.items():
        setattr(cls, k, integer_params_decorated(v))
    return cls


@integer_params
class Vector:
    def __init__(self, *args):
        self.__coords = list(args)

    def __getitem__(self, item):
        return self.__coords[item]

    def __setitem__(self, key, value):
        self.__coords[key] = value

    def set_coords(self, *coords, reverse=False):
        c = list(coords)
        self.__coords = c if not reverse else c[::-1]


class SoftList(list):
    def __getitem__(self, item):
        if not (0 <= item < len(self)) and not(-1 >= item >= -len(self)):
            return False
        return super(SoftList, self).__getitem__(item)

    def __setitem__(self, key, value):
        if not (0 <= key < len(self)) and not(-1 >= key >= -len(self)):
            return False
        super(SoftList, self).__setitem__(key, value)


class StringDigit(str):
    def __init__(self, string):
        if not all(i in '0123456789' for i in string):
            raise ValueError("в строке должны быть только цифры")
        self.string = string

    def __add__(self, other):
        if not all(i in '0123456789' for i in other):
            raise ValueError("в строке должны быть только цифры")
        return StringDigit(self.string + other)

    def __radd__(self, other):
        if not all(i in '0123456789' for i in other):
            raise ValueError("в строке должны быть только цифры")
        return StringDigit(other + self.string)


class ItemAttrs:
    def __init__(self, *args):
        self.items = list(args)

    def __getitem__(self, item):
        return self.items[item]

    def __setitem__(self, key, value):
        self.items[key] = value


class Point(ItemAttrs):
    def __init__(self, x, y):
        super(Point, self).__init__(x, y)
