from math import sqrt


class Car:
    __model = None

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, model):
        if type(model) is str and 2 <= len(model) <= 100:
            self.__model = model


class WindowDlg:
    def __init__(self, title, width, height):
        self.__title, self.__width, self.__height = title, width, height

    def show(self):
        print(f"{self.__title}: {self.__width}, {self.__height}")

    def get_width(self):
        return self.__width

    def set_width(self, width):
        if type(width) is int and 0 <= width <= 10000:
            self.__width = width
            self.show()

    def get_height(self):
        return self.__height

    def set_height(self, height):
        if type(height) is int and 0 <= height <= 10000:
            self.__height = height
            self.show()

    width = property(get_width, set_width)
    height = property(get_height, set_height)


class StackObj:
    def __init__(self, data):
        self.__data = data
        self.__next = None

    def get_next(self):
        return self.__next

    def set_next(self, nxt):
        if type(nxt) is StackObj or nxt is None:
            self.__next = nxt

    def get_data(self):
        return self.__data

    def set_data(self, data):
        self.__data = data

    def copy(self):
        return StackObj(self.__data)

    next = property(get_next, set_next)
    data = property(get_data, set_data)


class Stack:
    def __init__(self):
        self.top, self.obj1, self.obj2 = None, None, None

    def push(self, obj):
        if self.top is None:
            self.top = obj
            self.obj2 = self.top
        else:
            self.obj1 = self.obj2
            self.obj2.next = obj
            self.obj2 = self.obj2.next

    def pop(self):
        if self.top is not None:
            if self.top.next is None:
                self.top = None
            else:
                self.obj2 = self.obj1
                self.obj2.next = None

    def get_data(self):
        data = []
        obj = self.top
        while obj is not None:
            data.append(obj.data)
            obj = obj.next
        return data


class RadiusVector2D:
    MIN_COORD = -100
    MAX_COORD = 1024

    @classmethod
    def __check_value(cls, value):
        return type(value) in (float, int) and cls.MIN_COORD <= value <= cls.MAX_COORD

    def __init__(self, x=0, y=0):
        self.__x, self.__y = x, y

    def get_x(self):
        return self.__x

    def set_x(self, x):
        if self.__check_value(x):
            self.__x = x

    def get_y(self):
        return self.__y

    def set_y(self, y):
        if self.__check_value(y):
            self.__y = y

    @staticmethod
    def norm2(vector):
        return vector.y ** 2 + vector.y ** 2

    x = property(get_x, set_x)
    y = property(get_y, set_y)


class TreeObj:
    def __init__(self, indx, value=None):
        self.indx = indx
        self.value = value
        self.__left = None
        self.__right = None

    def get_left(self):
        return self.__left

    def set_left(self, left):
        self.__left = left

    def get_right(self):
        return self.__right

    def set_right(self, right):
        self.__right = right

    left = property(get_left, set_left)
    right = property(get_right, set_right)


class DecisionTree:
    root = None

    @classmethod
    def predict(cls, root, x):
        obj = root
        while (x[obj.indx] and obj.left) or (obj.right and not x[obj.indx]):
            obj = obj.left if x[obj.indx] else obj.right
        else:
            return obj.value

    @classmethod
    def add_obj(cls, obj, node=None, left=True):
        if cls.root is None:
            cls.root = obj
        else:
            if left is True:
                node.left = obj
            else:
                node.right = obj
        return obj


class PathLines:
    def __init__(self, *args):
        self.__lines = [LineTo(0, 0)] + list(args)

    def get_path(self):
        return self.__lines[1:]

    def get_length(self):
        length = 0
        for i in range(1, len(self.__lines)):
            length += sqrt((self.__lines[i].x - self.__lines[i - 1].x) ** 2 + (self.__lines[i].y -
                                                                               self.__lines[i - 1].y) ** 2)
        return length

    def add_line(self, line):
        self.__lines.append(line)


class LineTo:
    def __init__(self, x, y):
        self.x, self.y = x, y


class PhoneBook:
    def __init__(self):
        self.__phones = []

    def add_phone(self, phone):
        self.__phones.append(phone)

    def remove_phone(self, indx):
        del self.__phones[indx]

    def get_phone_list(self):
        return self.__phones


class PhoneNumber:
    def __init__(self, number, fio):
        self.number = number
        self.fio = fio
