import sys
from random import randint


class Player:
    def __init__(self, name, old, score):
        self.name = name
        self.old = old
        self.score = score

    def __bool__(self):
        return self.score > 0


class MailBox:
    def __init__(self):
        self.inbox_list = []

    def receive(self):
        lst_in = list(map(str.strip, sys.stdin.readlines()))
        for i in lst_in:
            self.inbox_list.append(MailItem(*i.split('; ')))


class MailItem:
    def __init__(self, mail_from, title, content):
        self.mail_from = mail_from
        self.title = title
        self.content = content
        self.is_read = False

    def set_read(self, fl_read):
        self.is_read = fl_read

    def __bool__(self):
        return self.is_read


class Line:
    def __init__(self, x1, y1, x2, y2):
        self.x1, self.y1, self.x2, self.y2 = x1, y1, x2, y2

    def __len__(self):
        return abs(int(((self.x2 - self.x1) ** 2 + (self.y2 - self.y1) ** 2) ** 0.5))


class Ellipse:
    def __init__(self, *args):
        if len(args) == 4:
            self.x1, self.y1, self.x2, self.y2 = args[0], args[1], args[2], args[3]

    def __bool__(self):
        return 'x1' in self.__dict__ and 'x2' in self.__dict__ and 'y1' in self.__dict__ and 'y2' in self.__dict__

    def get_coords(self):
        if not self:
            raise AttributeError('нет координат для извлечения')
        return self.x1, self.y1, self.x2, self.y2


class GamePole:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self, n, m, total_mines):
        self.N, self.M = n, m
        self.total_mines = total_mines
        self.__pole_cells = tuple([tuple([Cell() for _ in range(m)]) for _ in range(n)])

    def get_pole(self):
        return self.__pole_cells

    def get_mines_around(self, i, j):
        a, b = i + 1, j + 1
        pole = [list(i) for i in self.pole]
        for k in range(len(pole)):
            pole[k].insert(0, Cell())
            pole[k].append(Cell())
        pole.insert(0, [Cell() for _ in range(self.M + 2)])
        pole.append([Cell() for _ in range(self.M + 2)])
        mines = [pole[a - 1][b - 1].is_mine, pole[a][b - 1].is_mine, pole[a + 1][b - 1].is_mine,
                 pole[a - 1][b].is_mine, pole[a - 1][b + 1].is_mine, pole[a + 1][b + 1].is_mine,
                 pole[a][b + 1].is_mine, pole[a + 1][b].is_mine]
        return mines.count(True)

    def init_pole(self):
        while self.total_mines != 0:
            i = randint(0, self.N - 1)
            j = randint(0, self.M - 1)
            if not self.pole[i][j].is_mine:
                self.pole[i][j].is_mine = True
                self.total_mines -= 1
        for i in range(self.N):
            for j in range(self.M):
                if not self.pole[i][j].is_mine:
                    self.pole[i][j].number = self.get_mines_around(i, j)

    def open_cell(self, i, j):
        if type(i) != int or type(j) != int or i < 0 or j < 0 or j >= self.M or i >= self.N:
            raise IndexError('некорректные индексы i, j клетки игрового поля')
        self.pole[i][j].is_open = True

    def show_pole(self):
        for i in self.pole:
            for j in i:
                if j:
                    print('*' if j.is_mine else j.number, end=' ')
                else:
                    print('#', end=' ')
            print()

    pole = property(get_pole)


class Cell:
    def __init__(self):
        self.__is_mine = False
        self.__number = 0
        self.__is_open = False

    @property
    def is_mine(self):
        return self.__is_mine

    @is_mine.setter
    def is_mine(self, is_mine):
        if type(is_mine) != bool:
            raise ValueError("недопустимое значение атрибута")
        self.__is_mine = is_mine

    @property
    def number(self):
        return self.__number

    @number.setter
    def number(self, number):
        if type(number) != int or number < 0 or number > 8:
            raise ValueError("недопустимое значение атрибута")
        self.__number = number

    @property
    def is_open(self):
        return self.__is_open

    @is_open.setter
    def is_open(self, is_open):
        if type(is_open) != bool:
            raise ValueError("недопустимое значение атрибута")
        self.__is_open = is_open

    def __bool__(self):
        return not self.is_open


class Vector:
    def __init__(self, *args):
        self.coords = list(args)

    def __add__(self, other):
        if len(self.coords) != len(other.coords):
            raise ArithmeticError('размерности векторов не совпадают')
        return Vector(*[self.coords[i] + other.coords[i] for i in range(len(self.coords))])

    def __iadd__(self, other):
        if type(other) in (float, int):
            self.coords = [i + other for i in self.coords]
        else:
            if len(self.coords) != len(other.coords):
                raise ArithmeticError('размерности векторов не совпадают')
            self.coords = [self.coords[i] + other.coords[i] for i in range(len(self.coords))]
        return self

    def __sub__(self, other):
        if len(self.coords) != len(other.coords):
            raise ArithmeticError('размерности векторов не совпадают')
        return Vector(*[self.coords[i] - other.coords[i] for i in range(len(self.coords))])

    def __isub__(self, other):
        if type(other) in (float, int):
            self.coords = [i - other for i in self.coords]
        else:
            if len(self.coords) != len(other.coords):
                raise ArithmeticError('размерности векторов не совпадают')
            self.coords = [self.coords[i] - other.coords[i] for i in range(len(self.coords))]
        return self

    def __mul__(self, other):
        if len(self.coords) != len(other.coords):
            raise ArithmeticError('размерности векторов не совпадают')
        return Vector(*[self.coords[i] * other.coords[i] for i in range(len(self.coords))])

    def __eq__(self, other):
        if len(self.coords) != len(other.coords):
            raise ArithmeticError('размерности векторов не совпадают')
        for i in range(len(self.coords)):
            if self.coords[i] != other.coords[i]:
                return False
        return True
