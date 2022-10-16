class ListInteger(list):
    def __init__(self, lst):
        for i in lst:
            if type(i) != int:
                raise TypeError('можно передавать только целочисленные значения')
        super().__init__(lst)

    def __setitem__(self, key, value):
        if type(value) != int:
            raise TypeError('можно передавать только целочисленные значения')
        super().__setitem__(key, value)

    def append(self, obj):
        if type(obj) != int:
            raise TypeError('можно передавать только целочисленные значения')
        super().append(obj)


class Thing:
    def __init__(self, name, price, weight):
        self.name = name
        self.price = price
        self.weight = weight


class DictShop(dict):
    def __init__(self, things=None):
        if things is None:
            things = {}
        if type(things) != dict:
            raise TypeError('аргумент должен быть словарем')
        for i in things:
            if type(i) != Thing:
                raise TypeError('ключами могут быть только объекты класса Thing')
        super().__init__(things)

    def __setitem__(self, key, value):
        if type(key) != Thing:
            raise TypeError('ключами могут быть только объекты класса Thing')
        super().__setitem__(key, value)


class Protists:
    pass


class Plants(Protists):
    pass


class Animals(Protists):
    pass


class Mosses(Plants):
    pass


class Flowering(Plants):
    pass


class Worms(Animals):
    pass


class Mammals(Animals):
    pass


class Human(Mammals):
    pass


class Monkeys(Mammals):
    pass


class Monkey(Monkeys):
    def __init__(self, name, weight, old):
        self.name = name
        self.weight = weight
        self.old = old


class Person(Human):
    def __init__(self, name, weight, old):
        self.name = name
        self.weight = weight
        self.old = old


class Flower(Flowering):
    def __init__(self, name, weight, old):
        self.name = name
        self.weight = weight
        self.old = old


class Worm(Worms):
    def __init__(self, name, weight, old):
        self.name = name
        self.weight = weight
        self.old = old


class Tuple(tuple):
    def __add__(self, other):
        return Tuple(super().__add__(tuple(other)))


class VideoItem:
    def __init__(self, title, descr, path):
        self.title = title
        self.descr = descr
        self.path = path
        self.rating = VideoRating()


class VideoRating:
    def __init__(self):
        self.__rating = 0

    def get_rating(self):
        return self.__rating

    def set_rating(self, rating):
        if not (type(rating) is int and 0 <= rating <= 5):
            raise ValueError('неверное присваиваемое значение')
        self.__rating = rating

    rating = property(get_rating, set_rating)


class IteratorAttrs:
    def __init__(self, **kwargs):
        self.attrs = kwargs
        for key, value in kwargs.items():
            setattr(self, key, value)

    def __iter__(self):
        for key, value in self.attrs.items():
            yield key, value


class SmartPhone(IteratorAttrs):
    def __init__(self, model, size, memory):
        super().__init__(model=model, size=size, memory=memory)
