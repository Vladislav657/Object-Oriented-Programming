class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return f'Книга: {self.title}; {self.author}; {self.pages}'


class Model:
    def __init__(self):
        self.fields = None

    def query(self, **kwargs):
        self.fields = kwargs

    def __str__(self):
        if self.fields is None:
            return 'Model'
        return f'Model: {", ".join([i + " = " + str(self.fields[i]) for i in self.fields])}'


class WordString:
    def __init__(self, string=''):
        self.__string = string

    def get_str(self):
        return self.__string

    def set_str(self, string):
        self.__string = string

    string = property(get_str, set_str)

    def __len__(self):
        return len(self.__string.split())

    def __call__(self, *args, **kwargs):
        return self.__string.split()[args[0]]


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def add_obj(self, obj):
        if self.head is None:
            obj.index = 0
            self.head = obj
            self.tail = obj
            self.length += 1
        else:
            obj.index = self.length
            self.tail.set_next(obj)
            obj.set_prev(self.tail)
            self.tail = obj
            self.length += 1

    def get_obj(self, indx):
        obj = self.head
        if obj.index == indx:
            return obj
        while True:
            obj = obj.get_next()
            if obj.index == indx:
                return obj

    def remove_obj(self, indx):
        obj = self.get_obj(indx)
        if indx == 0:
            self.head = obj.get_next()
            self.head.set_prev(None)
            obj = obj.get_next()
            while obj is not None:
                obj.index -= 1
                obj = obj.get_next()
        elif indx == self.length - 1:
            self.tail = obj.get_prev()
            self.tail.set_next(None)
        else:
            obj.get_prev().set_next(obj.get_next())
            obj.get_next().set_prev(obj.get_prev())
            obj = obj.get_next()
            while obj is not None:
                obj.index -= 1
                obj = obj.get_next()
        self.length -= 1

    def __len__(self):
        return self.length

    def __call__(self, *args, **kwargs):
        obj = self.get_obj(args[0])
        return obj.get_data()


class ObjList:
    def __init__(self, data):
        self.__data = data
        self.__prev = None
        self.__next = None
        self.index = None

    def get_data(self):
        return self.__data

    def get_prev(self):
        return self.__prev

    def get_next(self):
        return self.__next

    def set_prev(self, prev):
        self.__prev = prev

    def set_next(self, nxt):
        self.__next = nxt


class Complex:
    def __init__(self, real, img):
        self.__real = real
        self.__img = img

    def __setattr__(self, key, value):
        if type(value) not in (float, int):
            raise ValueError("Неверный тип данных.")
        object.__setattr__(self, key, value)

    def __abs__(self):
        return (self.real ** 2 + self.img ** 2) ** 0.5

    def get_real(self):
        return self.__real

    def set_real(self, real):
        self.__real = real

    def get_img(self):
        return self.__img

    def set_img(self, img):
        self.__img = img

    real = property(get_real, set_real)
    img = property(get_img, set_img)


class RadiusVector:
    def __init__(self, *args):
        if len(args) == 1:
            self.coords = [0 for _ in range(args[0])]
        else:
            self.coords = list(args)

    def set_coords(self, *args):
        if len(args) < len(self.coords):
            for i in range(len(args)):
                self.coords[i] = args[i]
        else:
            for i in range(len(self.coords)):
                self.coords[i] = args[i]

    def get_coords(self):
        return tuple(self.coords)

    def __len__(self):
        return len(self.coords)

    def __abs__(self):
        return sum([i * i for i in self.coords]) ** 0.5


class DeltaClock:
    def __init__(self, clock1, clock2):
        self.clock1 = clock1
        self.clock2 = clock2

    def __len__(self):
        if self.clock1.get_time() - self.clock2.get_time() < 0:
            return 0
        return self.clock1.get_time() - self.clock2.get_time()

    def __str__(self):
        hours = str(len(self) // 60 // 60).rjust(2, '0')
        minutes = str(len(self) // 60 % 60).rjust(2, '0')
        seconds = str(len(self) % 60).rjust(2, '0')
        return f'{hours}: {minutes}: {seconds}'


class Clock:
    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def get_time(self):
        return self.hours * 3600 + self.minutes * 60 + self.seconds


class Recipe:
    def __init__(self, *args):
        self.ingredients = list(args)

    def add_ingredient(self, ing):
        self.ingredients.append(ing)

    def remove_ingredient(self, ing):
        self.ingredients.remove(ing)

    def get_ingredients(self):
        return tuple(self.ingredients)

    def __len__(self):
        return len(self.ingredients)


class Ingredient:
    def __init__(self, name, volume, measure):
        self.name = name
        self.volume = volume
        self.measure = measure

    def __str__(self):
        return f'{self.name}: {self.volume}, {self.measure}'


class PolyLine:
    def __init__(self, start_coord, *args):
        self.coords = [start_coord] + list(args)

    def add_coord(self, x, y):
        self.coords.append((x, y))

    def remove_coord(self, indx):
        del self.coords[indx]

    def get_coords(self):
        return self.coords
