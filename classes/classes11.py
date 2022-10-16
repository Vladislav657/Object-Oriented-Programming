class Record:
    def __init__(self, **kwargs):
        for i in kwargs:
            self.__dict__[i] = kwargs[i]

    def __getitem__(self, item):
        if type(item) != int or item < 0 or item >= len(self.__dict__.values()):
            raise IndexError('неверный индекс поля')
        return list(self.__dict__.values())[item]

    def __setitem__(self, key, value):
        if type(key) != int or key < 0 or key >= len(self.__dict__.keys()):
            raise IndexError('неверный индекс поля')
        self.__dict__[list(self.__dict__.keys())[key]] = value


class Track:
    def __init__(self, start_x, start_y):
        self.start_x = start_x
        self.start_y = start_y
        self.lines = []

    def add_point(self, x, y, speed):
        self.lines.append([(x, y), speed])

    def __getitem__(self, item):
        if type(item) is int and 0 <= item < len(self.lines):
            return self.lines[item][0], self.lines[item][1]
        raise IndexError('некорректный индекс')

    def __setitem__(self, key, value):
        if not (type(key) is int and 0 <= key < len(self.lines)):
            raise IndexError('некорректный индекс')
        self.lines[key][1] = value


class Array:
    def __init__(self, max_length, cell):
        self.max_length = max_length
        self.array = [cell(0) for _ in range(max_length)]

    def __getitem__(self, item):
        if not (type(item) == int and 0 <= item < self.max_length):
            raise IndexError('неверный индекс для доступа к элементам массива')
        return self.array[item].value

    def __setitem__(self, key, value):
        if not (type(key) == int and 0 <= key < self.max_length):
            raise IndexError('неверный индекс для доступа к элементам массива')
        self.array[key].value = value

    def __str__(self):
        return ' '.join([str(i.value) for i in self.array])


class Integer:
    def __init__(self, start_value):
        self.__value = start_value

    def get_value(self):
        return self.__value

    def set_value(self, value):
        if type(value) != int:
            raise ValueError('должно быть целое число')
        self.__value = value

    value = property(get_value, set_value)


class Float:
    def __init__(self, start_value):
        self.__value = start_value

    def get_value(self):
        return self.__value

    def set_value(self, value):
        if type(value) != float:
            raise ValueError('должно быть вещественное число')
        self.__value = value

    value = property(get_value, set_value)


class IntegerValue:
    def __set_name__(self, owner, name):
        self.name = '__' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        if type(value) != int:
            raise ValueError('возможны только целочисленные значения')
        setattr(instance, self.name, value)


class StringValue:
    def __set_name__(self, owner, name):
        self.name = '__' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        if type(value) != str:
            raise ValueError('возможны только строковые значения')
        setattr(instance, self.name, value)


class CellInteger:
    value = IntegerValue()

    def __init__(self, start_value=0):
        self.value = start_value


class CellString:
    value = StringValue()

    def __init__(self, start_value=''):
        self.value = start_value


class TableValues:
    def __init__(self, rows, cols, cell=None):
        if cell is None:
            raise ValueError('параметр cell не указан')
        self.cells = tuple([tuple([cell() for _ in range(cols)]) for _ in range(rows)])

    def __getitem__(self, item):
        return self.cells[item[0]][item[1]].value

    def __setitem__(self, key, value):
        self.cells[key[0]][key[1]].value = value


class StackObj:
    def __init__(self, data):
        self.data = data
        self.next = None

    def copy(self):
        obj = StackObj(self.data)
        obj.next = self.next
        return obj


class Stack:
    def __init__(self):
        self.top = None
        self.__bottom = None
        self.__count_obj = 0

    def push(self, obj):
        if self.top is None:
            self.top = obj
            self.__bottom = obj
        else:
            self.__bottom.next = obj
            self.__bottom = obj
        self.__count_obj += 1

    def pop(self):
        if self.top.next is None:
            obj = self.top.copy()
            self.top = None
            self.__bottom = None
        else:
            obj = self.top
            while obj.next != self.__bottom:
                obj = obj.next
            else:
                self.__bottom = obj
                obj = self.__bottom.next.copy()
                self.__bottom.next = None
        self.__count_obj -= 1
        return obj

    def __getitem__(self, item):
        if not (type(item) == int and 0 <= item < self.__count_obj):
            raise IndexError('неверный индекс')
        c = 0
        obj = self.top
        while True:
            if c == item:
                return obj
            c += 1
            obj = obj.next

    def __setitem__(self, key, value):
        if not (type(key) == int and 0 <= key < self.__count_obj):
            raise IndexError('неверный индекс')
        c = 0
        obj = self.top
        while True:
            if c == key:
                obj.data = value.data
                break
            c += 1
            obj = obj.next


class RadiusVector:
    def __init__(self, *args):
        self.coords = list(args)

    def __getitem__(self, item):
        if type(item) is int:
            return self.coords[item]
        return tuple(self.coords[item])

    def __setitem__(self, key, value):
        self.coords[key] = value


class TicTacToe:
    def __init__(self):
        self.pole = tuple([tuple([Cell1() for _ in range(3)]) for _ in range(3)])

    def clear(self):
        for i in range(3):
            for j in range(3):
                self.pole[i][j].is_free = True
                self.pole[i][j].value = 0

    def __getitem__(self, item):
        if type(item[0]) is int and 0 <= item[0] < 3 and type(item[1]) is int and 0 <= item[1] < 3:
            return self.pole[item[0]][item[1]].value
        elif type(item[0]) is int and 0 <= item[0] < 3 and type(item[1]) is slice:
            return tuple([i.value for i in self.pole[item[0]][item[1]]])
        elif type(item[1]) is int and 0 <= item[1] < 3 and type(item[0]) is slice:
            return tuple([i[item[1]].value for i in self.pole[item[0]]])
        else:
            raise IndexError('неверный индекс клетки')

    def __setitem__(self, key, value):
        if not (type(key[0]) == int and 0 <= key[0] < 3 and type(key[1]) == int and 0 <= key[1] < 3):
            raise IndexError('неверный индекс клетки')
        if not self.pole[key[0]][key[1]]:
            raise ValueError('клетка уже занята')
        self.pole[key[0]][key[1]].value = value
        self.pole[key[0]][key[1]].is_free = False


class Cell1:
    def __init__(self):
        self.is_free = True
        self.value = 0

    def __bool__(self):
        return self.is_free


class Bag:
    def __init__(self, max_weight):
        self.max_weight = max_weight
        self.things = []

    def add_thing(self, thing):
        if self.max_weight - thing.weight < 0:
            raise ValueError('превышен суммарный вес предметов')
        self.max_weight -= thing.weight
        self.things.append(thing)

    def __getitem__(self, item):
        if not (type(item) is int and 0 <= item < len(self.things)):
            raise IndexError('неверный индекс')
        return self.things[item]

    def __setitem__(self, key, value):
        if not (type(key) is int and 0 <= key < len(self.things)):
            raise IndexError('неверный индекс')
        if self.max_weight + (self.things[key].weight - value.weight) < 0:
            raise ValueError('превышен суммарный вес предметов')
        self.max_weight += (self.things[key].weight - value.weight)
        self.things[key] = value

    def __delitem__(self, key):
        if not (type(key) is int and 0 <= key < len(self.things)):
            raise IndexError('неверный индекс')
        self.max_weight += self.things[key].weight
        del self.things[key]


class Thing:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight


class SparseTable:
    def __init__(self):
        self.rows = 0
        self.cols = 0
        self.cells = {}

    def add_data(self, row, col, data):
        if col >= self.cols:
            self.cols = col + 1
        if row >= self.rows:
            self.rows = row + 1
        self.cells[(row, col)] = data

    def remove_data(self, row, col):
        if (row, col) not in self.cells.keys():
            raise IndexError('ячейка с указанными индексами не существует')
        del self.cells[(row, col)]
        self.rows = list(self.cells.keys())[0][0] + 1
        self.cols = list(self.cells.keys())[0][1] + 1
        for i in self.cells.keys():
            if i[0] >= self.rows:
                self.rows = i[0] + 1
            if i[1] >= self.cols:
                self.cols = i[1] + 1

    def __getitem__(self, item):
        if (item[0], item[1]) not in self.cells.keys():
            raise ValueError('данные по указанным индексам отсутствуют')
        return self.cells[(item[0], item[1])]

    def __setitem__(self, key, value):
        self.add_data(key[0], key[1], value)


class Cell2:
    def __init__(self, value):
        self.value = value
