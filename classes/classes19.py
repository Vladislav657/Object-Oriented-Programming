class Person:
    __slots__ = ('_fio', '_old', '_job')

    def __init__(self, fio, old, job):
        self._fio, self._old, self._job = fio, old, job


class Planet:
    def __init__(self, name, diametr, period_solar, period):
        self._name = name
        self._diametr = diametr
        self._period_solar = period_solar
        self._period = period


class SolarSystem:
    __slots__ = ('_mercury', '_venus', '_earth', '_mars', '_jupiter', '_saturn', '_uranus', '_neptune')
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        self._mercury = Planet('Меркурий', 4878, 87.97, 1407.5)
        self._venus = Planet('Венера', 12104, 224.7, 5832.45)
        self._earth = Planet('Земля', 12756, 365.3, 23.93)
        self._mars = Planet('Марс', 6794, 687, 24.62)
        self._jupiter = Planet('Юпитер', 142800, 4330, 9.9)
        self._saturn = Planet('Сатурн', 120660, 10753, 10.63)
        self._uranus = Planet('Уран', 51118, 30665, 17.2)
        self._neptune = Planet('Нептун', 49528, 60150, 16.1)


class Star:
    __slots__ = ('_name', '_massa', '_temp')

    def __init__(self, name, massa, temp):
        self._name = name
        self._massa = massa
        self._temp = temp


class WhiteDwarf(Star):
    __slots__ = ('_type_star', '_radius')

    def __init__(self, name, massa, temp, type_star, radius):
        super(WhiteDwarf, self).__init__(name, massa, temp)
        self._type_star = type_star
        self._radius = radius


class YellowDwarf(Star):
    __slots__ = ('_type_star', '_radius')
    
    def __init__(self, name, massa, temp, type_star, radius):
        super(YellowDwarf, self).__init__(name, massa, temp)
        self._type_star = type_star
        self._radius = radius


class RedGiant(Star):
    __slots__ = ('_type_star', '_radius')

    def __init__(self, name, massa, temp, type_star, radius):
        super(RedGiant, self).__init__(name, massa, temp)
        self._type_star = type_star
        self._radius = radius


class Pulsar(Star):
    __slots__ = ('_type_star', '_radius')

    def __init__(self, name, massa, temp, type_star, radius):
        super(Pulsar, self).__init__(name, massa, temp)
        self._type_star = type_star
        self._radius = radius


class Note:
    def __init__(self, name, ton=0):
        if name not in ('до', 'ре', 'ми', 'фа', 'соль', 'ля', 'си') or ton not in (-1, 0, 1):
            raise ValueError('недопустимое значение аргумента')
        self._name = name
        self._ton = ton

    def __setattr__(self, key, value):
        if key == '_name' and value not in ('до', 'ре', 'ми', 'фа', 'соль', 'ля', 'си') or key == '_ton' and value \
                not in (-1, 0, 1):
            raise ValueError('недопустимое значение аргумента')
        object.__setattr__(self, key, value)


class Notes:
    __slots__ = ('_do', '_re', '_mi', '_fa', '_solt', '_la', '_si')
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        self._do = Note('до')
        self._re = Note("ре")
        self._mi = Note("ми")
        self._fa = Note("фа")
        self._solt = Note("соль")
        self._la = Note("ля")
        self._si = Note("си")

    def __getitem__(self, item):
        if not (0 <= item < len(Notes.__slots__)):
            raise IndexError('недопустимый индекс')
        return getattr(self, Notes.__slots__[item])


class Function:
    def __init__(self):
        self._amplitude = 1.0     # амплитуда функции
        self._bias = 0.0          # смещение функции по оси Oy

    def __call__(self, x, *args, **kwargs):
        return self._amplitude * self._get_function(x) + self._bias

    def _get_function(self, x):
        raise NotImplementedError('метод _get_function должен быть переопределен в дочернем классе')

    def __add__(self, other):
        if type(other) not in (int, float):
            raise TypeError('смещение должно быть числом')
        obj = self.__class__(self)
        obj._bias = self._bias + other
        return obj

    def __mul__(self, other):
        if type(other) not in (int, float):
            raise TypeError('смещение должно быть числом')
        obj = self.__class__(self)
        obj._amplitude = self._amplitude * other
        return obj


class Linear(Function):
    def __init__(self, *args):
        super(Linear, self).__init__()
        if len(list(args)) == 1:
            self._k, self._b = args[0].get_k(), args[0].get_b()
        else:
            self._k, self._b = args[0], args[1]

    def get_k(self):
        return self._k

    def get_b(self):
        return self._b

    def _get_function(self, x):
        return self._k * x + self._b
