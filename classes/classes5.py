from random import randint


class RandomPassword:
    def __init__(self, psw_chars, min_length, max_length):
        self.psw_chars = psw_chars
        self.min_length = min_length
        self.max_length = max_length

    def __call__(self, *args, **kwargs):
        return ''.join([self.psw_chars[randint(0, len(self.psw_chars) - 1)] for _ in range(randint(self.min_length,
                                                                                                   self.max_length))])


def rand_pass(func):
    def wrapper(psw_chars, min_length, max_length):
        return func(psw_chars, min_length, max_length)
    return wrapper


@rand_pass
def gen_pass(psw_chars, min_length, max_length):
    return ''.join([psw_chars[randint(0, len(psw_chars) - 1)] for _ in range(randint(min_length, max_length))])


class ImageFileAcceptor:
    def __init__(self, extensions):
        self.extensions = extensions

    def __call__(self, *args, **kwargs):
        return args[0][args[0].index('.') + 1:] in self.extensions


class LengthValidator:
    def __init__(self, min_length, max_length):
        self.min_length = min_length
        self.max_length = max_length

    def __call__(self, *args, **kwargs):
        return self.min_length <= len(args[0]) <= self.max_length


class CharsValidator:
    def __init__(self, chars):
        self.chars = chars

    def __call__(self, *args, **kwargs):
        for i in args[0]:
            if i not in self.chars:
                return False
        return True


class RenderList:
    def __init__(self, type_list=''):
        self.type_list = type_list

    def __call__(self, *args, **kwargs):
        tag = 'ol' if self.type_list == 'ol' else 'ul'
        html = f'<{tag}>'
        for i in args[0]:
            html += f'\n<li>{i}</li>'
        html += f'\n</{tag}>'
        return html


class HandlerGET:
    def __init__(self, func):
        self.__fn = func

    @staticmethod
    def get(func, request):
        if 'method' not in request or request['method'] == 'GET':
            return f'GET: {func(request)}'
        else:
            return None

    def __call__(self, *args, **kwargs):
        return self.get(self.__fn, args[0])


class Handler:
    def __init__(self, methods=('GET',)):
        self.methods = methods

    @staticmethod
    def get(func, request):
        return f'GET: {func(request)}'

    @staticmethod
    def post(func, request):
        return f'POST: {func(request)}'

    def __call__(self, func):
        def wrapper(request):
            if ('method' not in request or request['method'] == 'GET') and 'GET' in self.methods:
                return self.get(func, request)
            elif request['method'] in self.methods and request['method'] == 'POST':
                return self.post(func, request)
            else:
                return None
        return wrapper


class InputDigits:
    def __init__(self, func):
        self.__fn = func

    def __call__(self, *args, **kwargs):
        return list(map(int, self.__fn().split()))


class InputValues:
    def __init__(self, render):
        self.render = render

    def __call__(self, func):
        def wrapper():
            return [self.render(i) for i in func().split()]
        return wrapper


class RenderDigit:
    def __call__(self, *args, **kwargs):
        if args[0][0] not in '-0123456789':
            return None
        for i in args[0][1:]:
            if i not in '0123456789':
                return None
        return int(args[0])


class Cell:
    def __init__(self, around_mines=0, mine=False, fl_open=False):
        self.around_mines = around_mines
        self.mine = mine
        self.fl_open = fl_open


class GamePole:
    def __init__(self, n, m):
        self.N = n
        self.M = m
        self.pole = [[Cell() for _ in range(n)] for _ in range(n)]
        self.init()

    def init(self):
        while self.M != 0:
            i = randint(0, self.N - 1)
            j = randint(0, self.N - 1)
            if self.pole[i][j].mine:
                continue
            else:
                self.pole[i][j].mine = True
                self.M -= 1
        else:
            self.round_pole()
            for i in range(1, self.N + 1):
                for j in range(1, self.N + 1):
                    self.pole[i][j].around_mines = self.count_mines(i, j)
            self.de_round_pole()

    def show(self):
        for i in self.pole:
            print(*[j.around_mines if j.fl_open else '#' for j in i])

    def round_pole(self):
        self.pole.insert(0, [Cell() for _ in range(self.N + 2)])
        self.pole.append([Cell() for _ in range(self.N + 2)])
        for i in range(1, self.N + 1):
            self.pole[i].insert(0, Cell())
            self.pole[i].append(Cell())

    def de_round_pole(self):
        del self.pole[0]
        del self.pole[-1]
        for i in range(self.N):
            del self.pole[i][0]
            del self.pole[i][-1]

    def count_mines(self, i, j):
        mines = [self.pole[i][j - 1].mine, self.pole[i][j + 1].mine, self.pole[i - 1][j].mine,
                 self.pole[i + 1][j].mine, self.pole[i - 1][j - 1].mine, self.pole[i + 1][j - 1].mine,
                 self.pole[i - 1][j + 1].mine, self.pole[i + 1][j + 1].mine]
        return mines.count(True)
