class Animal:
    def __init__(self, name, kind, old):
        self.__name = name
        self.__kind = kind
        self.__old = old

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_kind(self):
        return self.__kind

    def set_kind(self, kind):
        self.__kind = kind

    def get_old(self):
        return self.__old

    def set_old(self, old):
        self.__old = old

    name = property(get_name, set_name)
    kind = property(get_kind, set_kind)
    old = property(get_old, set_old)


class Furniture:
    def __init__(self, name, weight):
        self._name = name
        self._weight = weight
        self.__verify_name()
        self.__verify_weight()

    def __verify_name(self):
        if type(self._name) != str:
            raise TypeError('название должно быть строкой')

    def __verify_weight(self):
        if type(self._weight) != int or self._weight <= 0:
            raise TypeError('вес должен быть положительным числом')


class Closet(Furniture):
    def __init__(self, name, weight, tp, doors):
        super(Closet, self).__init__(name, weight)
        self._tp = tp
        self._doors = doors

    def get_attrs(self):
        return self._name, self._weight, self._tp, self._doors


class Chair(Furniture):
    def __init__(self, name, weight, height):
        super(Chair, self).__init__(name, weight)
        self._height = height

    def get_attrs(self):
        return self._name, self._weight, self._height


class Table(Furniture):
    def __init__(self, name, weight, height, square):
        super(Table, self).__init__(name, weight)
        self._height = height
        self._square = square

    def get_attrs(self):
        return self._name, self._weight, self._height, self._square


class Observer:
    def update(self, data):
        pass

    def __hash__(self):
        return hash(id(self))


class Subject:
    def __init__(self):
        self.__observers = {}
        self.__data = None

    def add_observer(self, observer):
        self.__observers[observer] = observer

    def remove_observer(self, observer):
        if observer in self.__observers:
            self.__observers.pop(observer)

    def __notify_observer(self):
        for ob in self.__observers:
            ob.update(self.__data)

    def change_data(self, data):
        self.__data = data
        self.__notify_observer()


class Data:
    def __init__(self, temp, press, wet):
        self.temp = temp    # температура
        self.press = press  # давление
        self.wet = wet      # влажность


class TemperatureView(Observer):
    def update(self, data):
        print(f"Текущая температура {data.temp}")


class PressureView(Observer):
    def update(self, data):
        print(f"Текущее давление {data.press}")


class WetView(Observer):
    def update(self, data):
        print(f"Текущая влажность {data.wet}")


class Aircraft:
    def __init__(self, model, mass, speed, top):
        if type(model) != str or type(mass) not in (int, float) or mass <= 0 or type(speed) not in (int, float) or \
                speed <= 0 or type(top) not in (int, float) or top <= 0:
            raise TypeError('неверный тип аргумента')
        self._model = model
        self._mass = mass
        self._speed = speed
        self._top = top


class PassengerAircraft(Aircraft):
    def __init__(self, model, mass, speed, top, chairs):
        super(PassengerAircraft, self).__init__(model, mass, speed, top)
        if type(chairs) != int or chairs <= 0:
            raise TypeError('неверный тип аргумента')
        self._chairs = chairs


class WarPlane(Aircraft):
    def __init__(self, model, mass, speed, top, weapons):
        super(WarPlane, self).__init__(model, mass, speed, top)
        if type(weapons) != dict or not all([type(i) == str for i in weapons.keys()] + [type(j) == int and j > 0 for j
                                                                                        in weapons.values()]):
            raise TypeError('неверный тип аргумента')
        self._weapons = weapons


def class_log(logs):
    def cls_decorator(cls):
        def func_decorator(func, name):
            def wrapper(*args, **kwargs):
                logs.append(name)
                return func(*args, **kwargs)
            return wrapper
        methods = {key: value for key, value in cls.__dict__.items() if callable(value)}
        for key, value in methods.items():
            setattr(cls, key, func_decorator(value, key))
        return cls
    return cls_decorator


vector_log = []


@class_log(vector_log)
class Vector:
    def __init__(self, *args):
        self.__coords = list(args)

    def __getitem__(self, item):
        return self.__coords[item]

    def __setitem__(self, key, value):
        self.__coords[key] = value


CURRENT_OS = 'windows'  # 'windows', 'linux'


class WindowsFileDialog:
    def __init__(self, title, path, exts):
        self.__title = title  # заголовок диалогового окна
        self.__path = path  # начальный каталог с файлами
        self.__exts = exts  # кортеж из отображаемых расширений файлов


class LinuxFileDialog:
    def __init__(self, title, path, exts):
        self.__title = title  # заголовок диалогового окна
        self.__path = path  # начальный каталог с файлами
        self.__exts = exts  # кортеж из отображаемых расширений файлов


class FileDialogFactory:
    def __new__(cls, *args, **kwargs):
        return cls.create_windows_filedialog(*args, **kwargs) if CURRENT_OS == 'windows' else \
            cls.create_linux_filedialog(*args, **kwargs)

    @staticmethod
    def create_windows_filedialog(title, path, exts):
        return WindowsFileDialog(title, path, exts)

    @staticmethod
    def create_linux_filedialog(title, path, exts):
        return LinuxFileDialog(title, path, exts)
