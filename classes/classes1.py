from random import randint, choice
from string import ascii_letters, digits


class Clock:
    def __init__(self, time=0):
        self.__time = 0
        if self.__check_time(time):
            self.__time = time

    def set_time(self, tm):
        if self.__check_time(tm):
            self.__time = tm

    def get_time(self):
        return self.__time

    @staticmethod
    def __check_time(tm):
        return type(tm) is int and 0 <= tm <= 100000


class Money:
    def __init__(self, money):
        self.__money = 0
        if self.__check_money(money):
            self.__money = money

    def set_money(self, money):
        if self.__check_money(money):
            self.__money = money

    def get_money(self):
        return self.__money

    def add_money(self, mn):
        self.__money += mn.get_money()

    @staticmethod
    def __check_money(money):
        return type(money) is int and money >= 0


class Book:
    def __init__(self, author, title, price):
        self.__author = author
        self.__title = title
        self.__price = price

    def set_title(self, title):
        self.__title = title

    def set_author(self, author):
        self.__author = author

    def set_price(self, price):
        self.__price = price

    def get_title(self):
        return self.__title

    def get_author(self):
        return self.__author

    def get_price(self):
        return self.__price


class Line:
    def __init__(self, x1, y1, x2, y2):
        self.__x1, self.__y1 = x1, y1
        self.__x2, self.__y2 = x2, y2

    def set_coords(self, x1, y1, x2, y2):
        self.__x1, self.__y1 = x1, y1
        self.__x2, self.__y2 = x2, y2

    def get_coords(self):
        return self.__x1, self.__y1, self.__x2, self.__y2

    def draw(self):
        print(self.__x1, self.__y1, self.__x2, self.__y2)


class Point:
    def __init__(self, x, y):
        self.__x, self.__y = x, y

    def get_coords(self):
        return self.__x, self.__y


class Rectangle:
    def __init__(self, *args):
        if len(args) == 2:
            self.__sp = args[0]
            self.__ep = args[1]
        else:
            self.__sp = Point(args[0], args[1])
            self.__ep = Point(args[2], args[3])

    def set_coords(self, sp, ep):
        self.__ep = ep
        self.__sp = sp

    def get_coords(self):
        return self.__sp, self.__ep

    def draw(self):
        print(f'Прямоугольник с координатами: {self.__sp.get_coords()} {self.__ep.get_coords()}')


class LinkedList:
    linked_list = []

    def __init__(self):
        self.head = None
        self.tail = None

    def add_obj(self, obj):
        self.linked_list.append(obj)
        if len(self.linked_list) == 1:
            self.head = obj
        self.tail = obj
        if len(self.linked_list) > 1:
            self.linked_list[-2].set_next(self.linked_list[-1])
            self.linked_list[-1].set_prev(self.linked_list[-2])

    def remove_obj(self):
        del self.linked_list[-1]
        if len(self.linked_list) == 0:
            self.head = None
            self.tail = None
        else:
            self.tail = self.linked_list[-1]
        if len(self.linked_list) > 0:
            self.linked_list[-1].set_next(None)

    def get_data(self):
        return [obj.get_data() for obj in self.linked_list]


class ObjList:
    def __init__(self, data):
        self.__data = data
        self.__next = None
        self.__prev = None

    def set_next(self, obj):
        self.__next = obj

    def set_prev(self, obj):
        self.__prev = obj

    def set_data(self, data):
        self.__data = data

    def get_next(self):
        return self.__next

    def get_prev(self):
        return self.__prev

    def get_data(self):
        return self.__data


class EmailValidator:
    def __new__(cls, *args, **kwargs):
        return None

    @classmethod
    def check_email(cls, email):
        if not cls.__is_email_str(email):
            return False
        chars = ascii_letters + digits + '_.@'
        for i in email:
            if i not in chars:
                return False
        if email.count('@') != 1:
            return False
        return len(email[:email.index('@')]) <= 100 and len(email[email.index('@'):]) < 52 and \
            '.' in email[email.index('@'):] and '..' not in email

    @classmethod
    def get_random_email(cls):
        chars = list(ascii_letters) + list(digits) + ['_', '.']
        email = ''
        for i in range(randint(1, 100)):
            email += choice(chars)
        email += '@gmail.com'
        return email

    @classmethod
    def __is_email_str(cls, email):
        return type(email) is str
