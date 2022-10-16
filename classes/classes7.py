class NewList:
    def __init__(self, lst=[]):
        self.lst = lst

    def __sub__(self, other):
        ls = other
        if type(ls) is NewList:
            ls = ls.lst.copy()
        nl = self.lst.copy()
        for i in range(len(ls)):
            if type(ls[i]) == bool:
                ls[i] = str(ls[i])

        for i in range(len(nl)):
            if type(nl[i]) == bool:
                nl[i] = str(nl[i])

        for i in ls:
            if i in nl:
                nl.remove(i)
        for i in range(len(nl)):
            if nl[i] == 'True':
                nl[i] = True
            elif nl[i] == 'False':
                nl[i] = False

        for i in range(len(ls)):
            if ls[i] == 'True':
                ls[i] = True
            elif ls[i] == 'False':
                ls[i] = False

        return NewList(nl)

    def __rsub__(self, other):
        return NewList(other) - self

    def get_list(self):
        return self.lst


class ListMath:
    def __init__(self, lst_math=[]):
        self.lst_math = [i for i in lst_math if type(i) in (int, float)]

    def __sub__(self, other):
        return ListMath([i - other for i in self.lst_math])

    def __rsub__(self, other):
        return ListMath([other - i for i in self.lst_math])

    def __add__(self, other):
        return ListMath([i + other for i in self.lst_math])

    def __radd__(self, other):
        return ListMath([i + other for i in self.lst_math])

    def __truediv__(self, other):
        return ListMath([i / other for i in self.lst_math])

    def __rtruediv__(self, other):
        return ListMath([other / i for i in self.lst_math])

    def __mul__(self, other):
        return ListMath([i * other for i in self.lst_math])

    def __rmul__(self, other):
        return ListMath([i * other for i in self.lst_math])


class Stack:
    def __init__(self):
        self.top = None
        self.__tail = None

    def push_back(self, obj):
        if self.top is None:
            self.top = obj
            self.__tail = obj
        else:
            self.__tail.set_next(obj)
            self.__tail = obj

    def pop_back(self):
        if self.top.get_next() is None:
            self.top = None
            self.__tail = None
        else:
            obj = self.top
            while obj.get_next() != self.__tail:
                obj = obj.get_next()
            else:
                self.__tail = obj
                self.__tail.set_next(None)

    def __add__(self, other):
        self.push_back(other)
        return self

    def __mul__(self, other):
        for i in other:
            self.push_back(StackObj(i))
        return self


class StackObj:
    def __init__(self, data):
        self.__data = data
        self.__next = None

    def get_next(self):
        return self.__next

    def set_next(self, nxt):
        self.__next = nxt


class Lib:
    def __init__(self):
        self.book_list = []

    def __add__(self, other):
        self.book_list.append(other)
        return self

    def __sub__(self, other):
        if type(other) is int:
            del self.book_list[other]
        else:
            self.book_list.remove(other)
        return self

    def __len__(self):
        return len(self.book_list)


class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year


class Budget:
    def __init__(self):
        self.items = []

    def add_item(self, it):
        self.items.append(it)

    def remove_item(self, indx):
        del self.items[indx]

    def get_items(self):
        return self.items


class Item:
    def __init__(self, name, money):
        self.name = name
        self.money = money

    def __add__(self, other):
        sm = other
        if type(sm) == Item:
            sm = sm.money
        self.money += sm
        return self.money

    def __radd__(self, other):
        return self + other


class Box3D:
    def __init__(self, width, height, depth):
        self.width = width
        self.height = height
        self.depth = depth

    def __add__(self, other):
        return Box3D(self.width + other.width, self.height + other.height, self.depth + other.depth)

    def __sub__(self, other):
        return Box3D(self.width - other.width, self.height - other.height, self.depth - other.depth)

    def __mul__(self, other):
        return Box3D(self.width * other, self.height * other, self.depth * other)

    def __rmul__(self, other):
        return self * other

    def __floordiv__(self, other):
        return Box3D(self.width // other, self.height // other, self.depth // other)

    def __mod__(self, other):
        return Box3D(self.width % other, self.height % other, self.depth % other)


class MaxPooling:
    def __init__(self, step=(2, 2), size=(2, 2)):
        self.step = step
        self.size = size

    def __create_mp(self, matrix):
        res = []
        for h in range(len(matrix) // self.step[1]):
            row = []
            for i in range(len(matrix[0]) // self.step[0]):
                window = []
                for j in range(self.size[1]):
                    for k in range(self.size[0]):
                        window.append(matrix[j + self.step[1] * h][k + self.step[0] * i])
                row.append(max(window))
            res.append(row)
        return res

    def __call__(self, *args, **kwargs):
        for i in range(1, len(args[0])):
            if len(args[0][i]) != len(args[0][i - 1]):
                raise ValueError("Неверный формат для первого параметра matrix.")
        for i in args[0]:
            for j in i:
                if type(j) not in (float, int):
                    raise ValueError("Неверный формат для первого параметра matrix.")
        return self.__create_mp(args[0])
