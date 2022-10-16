from abc import ABC, abstractmethod


class Student:
    def __init__(self, fio, group):
        self._fio = fio
        self._group = group
        self._lect_marks = []  # оценки за лекции
        self._house_marks = []  # оценки за домашние задания

    def add_lect_marks(self, mark):
        self._lect_marks.append(mark)

    def add_house_marks(self, mark):
        self._house_marks.append(mark)

    def __str__(self):
        return f"Студент {self._fio}: оценки на лекциях: {str(self._lect_marks)}; оценки за д/з: " \
               f"{str(self._house_marks)}"


class Mentor:
    def __init__(self, fio, subject):
        self._fio = fio
        self._subject = subject


class Lector(Mentor):
    def __init__(self, fio, subject):
        super(Lector, self).__init__(fio, subject)

    @staticmethod
    def set_mark(student, mark):
        student.add_lect_marks(mark)

    def __str__(self):
        return f'Лектор {self._fio}: предмет {self._subject}'


class Reviewer(Mentor):
    def __init__(self, fio, subject):
        super(Reviewer, self).__init__(fio, subject)

    @staticmethod
    def set_mark(student, mark):
        student.add_house_marks(mark)

    def __str__(self):
        return f'Эксперт {self._fio}: предмет {self._subject}'


class ShopInterface:
    def get_id(self):
        raise NotImplementedError('в классе не переопределен метод get_id')


class ShopItem(ShopInterface):
    id = 0

    def __init__(self, name, weight, price):
        self.__id = ShopItem.id
        self._name = name
        self._weight = weight
        self._price = price
        ShopItem.id += 1

    def get_id(self):
        return self.__id


class Validator:
    def _is_valid(self, data):
        raise NotImplementedError('в классе не переопределен метод _is_valid')


class FloatValidator(Validator):
    def __init__(self, min_value, max_value):
        self.min_value = min_value
        self.max_value = max_value

    def _is_valid(self, data):
        return type(data) is float and self.min_value <= data <= self.max_value

    def __call__(self, *args, **kwargs):
        return self._is_valid(args[0])


class Model(ABC):
    @abstractmethod
    def get_pk(self):
        pass

    @staticmethod
    def get_info():
        return "Базовый класс Model"


class ModelForm(Model):
    id = 0

    def __init__(self, login, password):
        self._id = ModelForm.id
        self._login = login
        self._password = password
        ModelForm.id += 1

    def get_pk(self):
        return self._id


class StackInterface(ABC):
    @abstractmethod
    def push_back(self, obj):
        pass

    @abstractmethod
    def pop_back(self):
        pass


class Stack(StackInterface):
    def __init__(self):
        self._top = None
        self._bottom = None

    def push_back(self, obj):
        if self._top is None:
            self._top = obj
        else:
            self._bottom.next = obj
        self._bottom = obj

    def pop_back(self):
        if self._top is None:
            return None
        if self._top.next is not None:
            obj = self._top
            while obj.next != self._bottom:
                obj = obj.next
            else:
                self._bottom = obj
                obj = self._bottom.next.copy()
                self._bottom.next = None
        else:
            obj = self._top.copy()
            self._top = None
            self._bottom = None
        return obj


class StackObj:
    def __init__(self, data):
        self._data = data
        self._next = None

    def get_next(self):
        return self._next

    def set_next(self, nxt):
        self._next = nxt

    def get_data(self):
        return self._data

    def copy(self):
        return StackObj(self._data)

    def __eq__(self, other):
        return self._data == other.get_data()

    next = property(get_next, set_next)


class CountryInterface(ABC):
    @property
    @abstractmethod
    def name(self):
        pass

    @name.setter
    @abstractmethod
    def name(self, name):
        pass

    @property
    @abstractmethod
    def population(self):
        pass

    @population.setter
    @abstractmethod
    def population(self, population):
        pass

    @property
    @abstractmethod
    def square(self):
        pass

    @square.setter
    @abstractmethod
    def square(self, square):
        pass

    @abstractmethod
    def get_info(self):
        pass


class Country(CountryInterface):
    def __init__(self, name, population, square):
        self._name = name
        self._population = population
        self._square = square

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def population(self):
        return self._population

    @population.setter
    def population(self, population):
        self._population = population

    @property
    def square(self):
        return self._square

    @square.setter
    def square(self, square):
        self._square = square

    def get_info(self):
        return f"{self.name}: {self.square}, {self.population}"


class Track:
    def __init__(self, *args):
        self.__points = []
        if len(args) == 2:
            self.__points.append(None)
        else:
            self.__points += list(args)

    def get_points(self):
        return tuple(self.__points)

    def add_back(self, pt):
        self.__points.append(pt)

    def add_front(self, pt):
        self.__points.insert(0, pt)

    def pop_back(self):
        del self.__points[-1]

    def pop_front(self):
        del self.__points[0]

    points = property(get_points)


class PointTrack:
    def __init__(self, x, y):
        if type(x) not in (float, int) or type(y) not in (float, int):
            raise TypeError('координаты должны быть числами')
        self.x, self.y = x, y

    def __str__(self):
        return f"PointTrack: {self.x}, {self.y}"


class Food:
    def __init__(self, name, weight, calories):
        self._name = name
        self._weight = weight
        self._calories = calories


class BreadFood(Food):
    def __init__(self, name, weight, calories, white):
        super(BreadFood, self).__init__(name, weight, calories)
        self._white = white


class SoupFood(Food):
    def __init__(self, name, weight, calories, dietary):
        super(SoupFood, self).__init__(name, weight, calories)
        self._dietary = dietary


class FishFood(Food):
    def __init__(self, name, weight, calories, fish):
        super(FishFood, self).__init__(name, weight, calories)
        self._fish = fish
