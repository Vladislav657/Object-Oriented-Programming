class CellInteger:
    def __init__(self, min_value, max_value):
        self._min_value = min_value
        self._max_value = max_value
        self._value = None

    def get_value(self):
        return self._value

    def set_value(self, value):
        if not self._min_value <= value <= self._max_value:
            raise CellIntegerException('значение выходит за допустимый диапазон')
        self._value = value

    value = property(get_value, set_value)


class CellFloat:
    def __init__(self, min_value, max_value):
        self._min_value = min_value
        self._max_value = max_value
        self._value = None

    def get_value(self):
        return self._value

    def set_value(self, value):
        if not self._min_value <= value <= self._max_value:
            raise CellFloatException('значение выходит за допустимый диапазон')
        self._value = value

    value = property(get_value, set_value)


class CellString:
    def __init__(self, min_length, max_length):
        self._min_length = min_length
        self._max_length = max_length
        self._value = None

    def get_value(self):
        return self._value

    def set_value(self, value):
        if not self._min_length <= len(value) <= self._max_length:
            raise CellStringException('длина строки выходит за допустимый диапазон')
        self._value = value

    value = property(get_value, set_value)


class CellException(Exception):
    __doc__ = '''CellException'''


class CellIntegerException(CellException):
    __doc__ = '''CellIntegerException'''


class CellFloatException(CellException):
    __doc__ = '''CellFloatException'''


class CellStringException(CellException):
    __doc__ = '''CellStringException'''


class TupleData:
    def __init__(self, *args):
        self.cells = list(args)

    def __getitem__(self, item):
        if not 0 <= item <= len(self.cells) - 1:
            raise IndexError
        return self.cells[item]

    def __setitem__(self, key, value):
        if not 0 <= key <= len(self.cells) - 1:
            raise IndexError
        self.cells[key] = value

    def __len__(self):
        return len(self.cells)

    def __iter__(self):
        self.index = -1
        return self

    def __next__(self):
        if self.index + 1 <= len(self.cells) - 1:
            self.index += 1
            return self.cells[self.index]
        raise StopIteration


class PrimaryKey:
    pk = 0

    def __init__(self):
        self.pk = PrimaryKey.pk
        PrimaryKey.pk += 1

    def __enter__(self):
        print("вход")

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(exc_type)
        return True


class DatabaseConnection:
    def __init__(self):
        self._fl_connection_open = None

    def connect(self):
        self._fl_connection_open = True

    def close(self):
        self._fl_connection_open = False

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()


class Box:
    def __init__(self, name, max_weight):
        self._name = name
        self._max_weight = max_weight
        self._things = []

    def get_things(self):
        return self._things

    def add_thing(self, obj):
        if self._max_weight - obj[1] < 0:
            raise ValueError('превышен суммарный вес вещей')
        self._max_weight -= obj[1]
        self._things.append(obj)

    def copy(self):
        return Box(self._name, self._max_weight)

    def change(self, odj):
        self._things += odj.get_things()


class BoxDefender:
    def __init__(self, box):
        self._box = box

    def __enter__(self):
        self._temp = self._box.copy()
        return self._temp

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            self._box.change(self._temp)
