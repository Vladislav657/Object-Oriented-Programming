class Person:
    def __init__(self, fio, job, old, salary, year_job):
        self.fio, self.job, self.old = fio, job, old
        self.salary, self.year_job = salary, year_job
        self.data = [self.fio, self.job, self.old, self.salary, self.year_job]

    def __getitem__(self, item):
        if not (type(item) == int and 0 <= item <= 4):
            raise IndexError('неверный индекс')
        return self.data[item]

    def __setitem__(self, key, value):
        if not (type(key) == int and 0 <= key <= 4):
            raise IndexError('неверный индекс')
        self.data[key] = value

    def __iter__(self):
        self.count = 0
        return self

    def __next__(self):
        if self.count < 5:
            self.value = self.data[self.count]
            self.count += 1
        else:
            raise StopIteration
        return self.value


class TriangleListIterator:
    def __init__(self, lst):
        self.lst = lst

    def __iter__(self):
        self.count, self.index = 1, 0
        return self

    def __next__(self):
        if self.index < self.count:
            self.value = self.lst[self.count - 1][self.index]
            self.index += 1
        elif not (self.count < len(self.lst)):
            raise StopIteration
        if not (self.index < self.count) and self.count < len(self.lst):
            self.count += 1
            self.index = 0
        return self.value


class IterColumn:
    def __init__(self, lst, column):
        self.lst = lst
        self.column = column

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index < len(self.lst):
            self.value = self.lst[self.index][self.column]
            self.index += 1
        else:
            raise StopIteration
        return self.value


class Stack:
    def __init__(self):
        self.top = None
        self.__bottom = None
        self.__count_obj = 0

    def push_back(self, obj):
        if self.top is None:
            self.top = obj
            self.__bottom = obj
        else:
            self.__bottom.next = obj
            self.__bottom = obj
        self.__count_obj += 1

    def push_front(self, obj):
        obj.next = self.top
        self.top = obj
        self.__count_obj += 1

    def __getitem__(self, item):
        if not (type(item) == int and 0 <= item < self.__count_obj):
            raise IndexError('неверный индекс')
        c = 0
        obj = self.top
        while True:
            if c == item:
                return obj.data
            c += 1
            obj = obj.next

    def __setitem__(self, key, value):
        if not (type(key) == int and 0 <= key < self.__count_obj):
            raise IndexError('неверный индекс')
        c = 0
        obj = self.top
        while True:
            if c == key:
                obj.data = value
                break
            c += 1
            obj = obj.next

    def __len__(self):
        return self.__count_obj

    def __iter__(self):
        self.value = StackObj('')
        self.value.next = self.top
        return self

    def __next__(self):
        if self.value.next is not None:
            self.value = self.value.next
        else:
            raise StopIteration
        return self.value


class StackObj:
    def __init__(self, data):
        self.data = data
        self.next = None


class TableValues:
    def __init__(self, rows, cols, type_data=int):
        self.rows = rows
        self.cols = cols
        self.type_data = type_data
        self.table = [[Cell(0) for _ in range(cols)] for _ in range(rows)]

    def __getitem__(self, item):
        if not (type(item[0]) == int and 0 <= item[0] < self.rows and type(item[1]) == int and 0 <= item[1] <
                self.cols):
            raise IndexError('неверный индекс')
        return self.table[item[0]][item[1]].data

    def __setitem__(self, key, value):
        if not (type(key[0]) == int and 0 <= key[0] < self.rows and type(key[1]) == int and 0 <= key[1] < self.cols):
            raise IndexError('неверный индекс')
        if type(value) != self.type_data:
            raise TypeError('неверный тип присваиваемых данных')
        self.table[key[0]][key[1]].data = value

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index < len(self.table):
            self.value = self.table[self.index]
            self.index += 1
        else:
            raise StopIteration
        return map(abs, self.value)


class Cell:
    def __init__(self, data):
        self.__data = data

    def get_data(self):
        return self.__data

    def set_data(self, data):
        self.__data = data

    def __abs__(self):
        return self.data

    data = property(get_data, set_data)


class Matrix:
    def __init__(self, *args):
        if len(args) == 1:
            for row in args[0]:
                for i in row:
                    if type(i) not in (int, float) or len(row) != len(args[0][0]):
                        raise TypeError('список должен быть прямоугольным, состоящим из чисел')
            self.matrix = args[0]
            self.rows = len(self.matrix)
            self.cols = len(self.matrix[0])
        else:
            if type(args[0]) != int or type(args[1]) != int or type(args[2]) not in (int, float):
                raise TypeError('аргументы rows, cols - целые числа; fill_value - произвольное число')
            self.matrix = [[args[2] for _ in range(args[1])] for _ in range(args[0])]
            self.rows = args[0]
            self.cols = args[1]

    def __getitem__(self, item):
        if not (type(item[0]) == int and 0 <= item[0] < self.rows and type(item[1]) == int and 0 <= item[1] <
                self.cols):
            raise IndexError('недопустимые значения индексов')
        return self.matrix[item[0]][item[1]]

    def __setitem__(self, key, value):
        if not (type(key[0]) == int and 0 <= key[0] < self.rows and type(key[1]) == int and 0 <= key[1] < self.cols):
            raise IndexError('недопустимые значения индексов')
        if type(value) not in (int, float):
            raise TypeError('значения матрицы должны быть числами')
        self.matrix[key[0]][key[1]] = value

    def __add__(self, other):
        if type(other) in (int, float):
            return Matrix([[i + other for i in j] for j in self.matrix])
        else:
            if len(self.matrix) != len(other.matrix) or len(self.matrix[0]) != len(other.matrix[0]):
                raise ValueError('операции возможны только с матрицами равных размеров')
            rows = len(self.matrix)
            cols = len(self.matrix[0])
            return Matrix([[self.matrix[i][j] + other.matrix[i][j] for j in range(cols)] for i in range(rows)])

    def __sub__(self, other):
        if type(other) in (int, float):
            return Matrix([[i - other for i in j] for j in self.matrix])
        else:
            if not (len(self.matrix) == len(other.matrix) and len(self.matrix[0]) == len(other.matrix[0])):
                raise ValueError('операции возможны только с матрицами равных размеров')
            rows = len(self.matrix)
            cols = len(self.matrix[0])
            return Matrix([[self.matrix[i][j] - other.matrix[i][j] for j in range(cols)] for i in range(rows)])
