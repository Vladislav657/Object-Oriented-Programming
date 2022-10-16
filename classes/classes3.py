class FloatValue:
    @classmethod
    def __check_value(cls, value):
        if type(value) != float:
            raise TypeError("Присваивать можно только вещественный тип данных.")

    def __set_name__(self, owner, name):
        self.name = '__' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        self.__check_value(value)
        setattr(instance, self.name, value)


class Cell:
    value = FloatValue()

    def __init__(self, start):
        self.value = start


class TableSheet:
    def __init__(self, n, m):
        self.cells = [[Cell(0.0) for _ in range(m)] for _ in range(n)]


class ValidateString:
    def __init__(self, min_length, max_length):
        self.min_length = min_length
        self.max_length = max_length

    def validate(self, string):
        return type(string) is str and self.min_length <= len(string) <= self.max_length


class StringValue:
    def __init__(self, min_length, max_length):
        self.min_length = min_length
        self.max_length = max_length

    def __set_name__(self, owner, name):
        self.name = '__' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        if type(value) is str and self.min_length <= len(value) <= self.max_length:
            setattr(instance, self.name, value)


class RegisterForm:
    login = StringValue(min_length=3, max_length=100)
    password = StringValue(min_length=3, max_length=100)
    email = StringValue(min_length=3, max_length=100)

    def __init__(self, login, password, email):
        self.login = login
        self.password = password
        self.email = email

    def get_fields(self):
        return [self.login, self.password, self.email]

    def show(self):
        print(f'<form>\nЛогин: {self.login}\nПароль: {self.password}\nEmail: {self.email}\n</form>')


class SuperShop:
    def __init__(self, name):
        self.name = name
        self.goods = []

    def add_product(self, product):
        self.goods.append(product)

    def remove_product(self, product):
        self.goods.remove(product)


class PriceValue:
    def __init__(self, max_length):
        self.max_length = max_length

    def __set_name__(self, owner, name):
        self.name = '__' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        if type(value) in (int, float) and 0 <= value <= self.max_length:
            setattr(instance, self.name, value)


class Product:
    name = StringValue(2, 50)
    price = PriceValue(10000)

    def __init__(self, name, price):
        self.name = name
        self.price = price


class Bag:
    def __init__(self, max_weight):
        self.max_weight = max_weight
        self.__things = []

    @property
    def things(self):
        return self.__things

    def add_thing(self, thing):
        if sum([thing.weight for thing in self.__things]) + thing.weight <= self.max_weight:
            self.__things.append(thing)

    def remove_thing(self, indx):
        del self.__things[indx]

    def get_total_weight(self):
        return sum([thing.weight for thing in self.__things])


class Thing:
    def __init__(self, name, weight):
        self.name, self.weight = name, weight


class TVProgram:
    def __init__(self, name):
        self.name = name
        self.items = []

    def add_telecast(self, tl):
        self.items.append(tl)

    def remove_telecast(self, indx):
        del self.items[indx - 1]


class Telecast:
    def __init__(self, uid, name, duration):
        self.__id = uid
        self.__name = name
        self.__duration = duration

    @property
    def uid(self):
        return self.__id

    @uid.setter
    def uid(self, uid):
        self.__id = uid

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def duration(self):
        return self.__duration

    @duration.setter
    def duration(self, duration):
        self.__duration = duration
