import time


class Book:
    def __init__(self, title='', author='', pages=0, year=0):
        self.title = title
        self.author = author
        self.pages = pages
        self.year = year

    def __setattr__(self, key, value):
        if key in ('title', 'author') and type(value) == str or key in ('pages', 'year') and type(value) == int:
            object.__setattr__(self, key, value)
        else:
            raise TypeError("Неверный тип присваиваемых данных.")


class Shop:
    def __init__(self, name):
        self.name = name
        self.goods = []

    def add_product(self, product):
        self.goods.append(product)

    def remove_product(self, product):
        self.goods.remove(product)


class Product:
    id = 0

    def __new__(cls, *args, **kwargs):
        cls.id += 1
        return super().__new__(cls)

    def __init__(self, name, weight, price):
        self.name = name
        self.weight = weight
        self.price = price

    def __setattr__(self, key, value):
        if key in ('id', 'weight', 'price') and type(value) == int and value >= 0 or key == 'name' and \
                type(value) == str:
            object.__setattr__(self, key, value)
        else:
            raise TypeError("Неверный тип присваиваемых данных.")

    def __delattr__(self, item):
        if item == 'id':
            raise AttributeError("Атрибут id удалять запрещено.")
        else:
            object.__delattr__(self, item)


class Course:
    def __init__(self, name):
        self.name = name
        self.modules = []

    def add_module(self, module):
        self.modules.append(module)

    def remove_module(self, index):
        del self.modules[index]


class Module:
    def __init__(self, name):
        self.name = name
        self.lessons = []

    def add_lesson(self, lesson):
        self.lessons.append(lesson)

    def remove_lesson(self, index):
        del self.lessons[index]


class LessonItem:
    def __init__(self, title, practices, duration):
        self.title = title
        self.practices = practices
        self.duration = duration

    def __setattr__(self, key, value):
        if key == 'title' and type(value) == str or (key == 'practices' or key == 'duration') and type(value) == int \
                and value >= 0:
            object.__setattr__(self, key, value)
        else:
            raise TypeError("Неверный тип присваиваемых данных.")

    def __getattr__(self, item):
        return False

    def __delattr__(self, item):
        return None


class Museum:
    def __init__(self, name):
        self.name = name
        self.exhibits = []

    def add_exhibit(self, obj):
        self.exhibits.append(obj)

    def remove_exhibit(self, obj):
        self.exhibits.remove(obj)

    def get_info_exhibit(self, index):
        return f'Описание экспоната {self.exhibits[index].name}: {self.exhibits[index].descr}'


class Picture:
    def __init__(self, name, author, descr):
        self.name = name
        self.author = author
        self.descr = descr


class Mummies:
    def __init__(self, name, location, descr):
        self.name = name
        self.author = location
        self.descr = descr


class Papyri:
    def __init__(self, name, date, descr):
        self.name = name
        self.author = date
        self.descr = descr


class SmartPhone:
    def __init__(self, model):
        self.model = model
        self.apps = []

    def add_app(self, app):
        if app.name not in [i.name for i in self.apps]:
            self.apps.append(app)

    def remove_app(self, app):
        self.apps.remove(app)


class AppVK:
    def __init__(self):
        self.name = "ВКонтакте"


class AppYouTube:
    def __init__(self, memory_max):
        self.name = "YouTube"
        self.memory_max = memory_max


class AppPhone:
    def __init__(self, phone_list):
        self.name = "Phone"
        self.phone_list = phone_list


class Circle:
    def __init__(self, x, y, radius):
        self.__x = x
        self.__y = y
        self.__radius = radius

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        self.__y = y

    @property
    def radius(self):
        return self.__radius

    @radius.setter
    def radius(self, radius):
        self.__radius = radius

    def __setattr__(self, key, value):
        if type(value) not in (float, int):
            raise TypeError("Неверный тип присваиваемых данных.")
        elif key == '_Circle__radius' and value > 0 or key in ('_Circle__x', '_Circle__y'):
            object.__setattr__(self, key, value)

    def __getattr__(self, item):
        return False


class Dimensions:
    MIN_DIMENSION = 10
    MAX_DIMENSION = 1000

    def __init__(self, a, b, c):
        self.__a = a
        self.__b = b
        self.__c = c

    @property
    def a(self):
        return self.__a

    @a.setter
    def a(self, a):
        self.__a = a

    @property
    def b(self):
        return self.__b

    @b.setter
    def b(self, b):
        self.__b = b

    @property
    def c(self):
        return self.__c

    @c.setter
    def c(self, c):
        self.__c = c

    def __setattr__(self, key, value):
        if key in ('MIN_DIMENSION', 'MAX_DIMENSION'):
            raise AttributeError("Менять атрибуты MIN_DIMENSION и MAX_DIMENSION запрещено.")
        elif self.MIN_DIMENSION <= value <= self.MAX_DIMENSION:
            object.__setattr__(self, key, value)


class GeyserClassic:
    MAX_DATE_FILTER = 100
    slot_1, slot_2, slot_3 = None, None, None

    def add_filter(self, slot_num, filt):
        if slot_num == 1 and self.slot_1 is None and type(filt) == Mechanical:
            self.slot_1 = filt
        elif slot_num == 2 and self.slot_2 is None and type(filt) == Aragon:
            self.slot_2 = filt
        elif slot_num == 3 and self.slot_3 is None and type(filt) == Calcium:
            self.slot_3 = filt

    def remove_filter(self, slot_num):
        if slot_num == 1:
            self.slot_1 = None
        elif slot_num == 2:
            self.slot_2 = None
        elif slot_num == 3:
            self.slot_3 = None

    def get_filters(self):
        return self.slot_1, self.slot_2, self.slot_3

    def water_on(self):
        return self.slot_1 is not None and self.slot_2 is not None and self.slot_3 is not None and 0 <= time.time() - \
               self.slot_1.date <= self.MAX_DATE_FILTER and 0 <= time.time() - self.slot_2.date <= self.MAX_DATE_FILTER\
               and 0 <= time.time() - self.slot_3.date <= self.MAX_DATE_FILTER


class Mechanical:
    def __init__(self, date):
        self.date = date

    def __setattr__(self, key, value):
        if key == 'date' and 'date' not in self.__dict__:
            object.__setattr__(self, key, value)


class Aragon:
    def __init__(self, date):
        self.date = date

    def __setattr__(self, key, value):
        if key == 'date' and 'date' not in self.__dict__:
            object.__setattr__(self, key, value)


class Calcium:
    def __init__(self, date):
        self.date = date

    def __setattr__(self, key, value):
        if key == 'date' and 'date' not in self.__dict__:
            object.__setattr__(self, key, value)
