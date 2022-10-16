from random import randint


class TicTacToe:
    FREE_CELL = 0
    HUMAN_X = 1
    COMPUTER_O = 2

    def __init__(self):
        self.pole = tuple([tuple([Cell() for _ in range(3)]) for _ in range(3)])
        self.__is_human_win = False
        self.__is_computer_win = False
        self.__is_draw = False

    def get_is_human_win(self):
        return self.__is_human_win

    def set_is_human_win(self, fl):
        self.__is_human_win = fl

    def get_is_computer_win(self):
        return self.__is_computer_win

    def set_is_computer_win(self, fl):
        self.__is_computer_win = fl

    def get_is_draw(self):
        return self.__is_draw

    def set_is_draw(self, fl):
        self.__is_draw = fl

    is_human_win = property(get_is_human_win, set_is_human_win)
    is_computer_win = property(get_is_computer_win, set_is_computer_win)
    is_draw = property(get_is_draw, set_is_draw)

    def __getitem__(self, item):
        if not (type(item[0]) == int and 0 <= item[0] < 3 and type(item[1]) == int and 0 <= item[1] < 3):
            raise IndexError('некорректно указанные индексы')
        return self.pole[item[0]][item[1]].value

    def __setitem__(self, key, value):
        if not (type(key[0]) == int and 0 <= key[0] < 3 and type(key[1]) == int and 0 <= key[1] < 3):
            raise IndexError('некорректно указанные индексы')
        self.pole[key[0]][key[1]].value = value
        self.end_game()

    def is_pole_filled(self):
        for i in range(3):
            for j in range(3):
                if self[i, j] == self.FREE_CELL:
                    return False
        return True

    def is_player_win(self, player):
        return self[0, 0] == self[0, 1] == self[0, 2] == player or self[1, 0] == self[1, 1] == self[1, 2] == player or \
               self[2, 0] == self[2, 1] == self[2, 2] == player or self[0, 0] == self[1, 0] == self[2, 0] == player or \
               self[0, 1] == self[1, 1] == self[2, 1] == player or self[0, 2] == self[1, 2] == self[2, 2] == player or \
               self[0, 0] == self[1, 1] == self[2, 2] == player or self[0, 2] == self[1, 1] == self[2, 0] == player

    def end_game(self):
        if self.is_player_win(self.HUMAN_X):
            self.is_human_win = self.is_player_win(self.HUMAN_X)
        elif self.is_player_win(self.COMPUTER_O):
            self.is_computer_win = self.is_player_win(self.COMPUTER_O)
        elif self.is_pole_filled():
            self.is_draw = self.is_pole_filled()

    def init(self):
        for i in range(3):
            for j in range(3):
                self[i, j] = self.FREE_CELL
        self.is_draw = False
        self.is_computer_win = False
        self.is_human_win = False

    def show(self):
        for i in range(3):
            for j in range(3):
                if self[i, j] == self.HUMAN_X:
                    print('X', end=' ')
                elif self[i, j] == self.COMPUTER_O:
                    print('O', end=' ')
                else:
                    print('#', end=' ')
            print()
        print()

    def human_go(self):
        if self:
            while True:
                coords = list(map(int, input().split()))
                i, j = coords[0], coords[1]
                if self[i, j] == self.FREE_CELL:
                    self[i, j] = self.HUMAN_X
                    break
                else:
                    print('Эта клетка уже занята.')
                    continue

    def computer_go(self):
        if self:
            while True:
                i = randint(0, 2)
                j = randint(0, 2)
                if self[i, j] == self.FREE_CELL:
                    self[i, j] = self.COMPUTER_O
                    break

    def __bool__(self):
        return not self.is_computer_win and not self.is_human_win and not self.is_draw


class Cell:
    def __init__(self):
        self.value = 0

    def __bool__(self):
        return self.value == 0
