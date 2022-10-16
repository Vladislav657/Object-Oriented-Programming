from random import randint, choice


class Ship:
    def __init__(self, length, tp=1, x=None, y=None):
        self._x, self._y = x, y
        self._length = length
        self._tp = tp
        self._is_move = True
        self._cells = [1] * length

    def is_ship_move(self):
        return self._is_move

    def get_cells(self):
        return self._cells

    def hit_ship(self):
        self._is_move = False

    def get_tp(self):
        return self._tp

    def set_start_coords(self, x, y):
        self._x, self._y = x, y

    def get_start_coords(self):
        return self._x, self._y

    def move(self, go):
        if self._is_move:
            if self._tp == 1:
                self._x += go
            else:
                self._y += go

    def get_length(self):
        return self._length

    def is_collide(self, ship):
        if self._x is None or self._y is None or ship.get_start_coords()[0] is None or ship.get_start_coords()[1] is \
                None:
            return False
        return self.get_tp() == 1 and ship.get_tp() == 2 and self._x - 1 <= ship.get_start_coords()[0] <= self._x + \
            self._length and ship.get_start_coords()[1] - 1 <= self._y <= ship.get_start_coords()[1] + \
            ship.get_length() or self.get_tp() == 2 and ship.get_tp() == 1 and self._y - 1 <= \
            ship.get_start_coords()[1] <= self._y + self._length and ship.get_start_coords()[0] - 1 <= self._x <= \
            ship.get_start_coords()[0] + ship.get_length() or self.get_tp() == 1 and ship.get_tp() == 1 and \
            self._y - 1 <= ship.get_start_coords()[1] <= self._y + 1 and \
            (ship.get_start_coords()[0] - 1 <= self._x <= ship.get_start_coords()[0] + ship.get_length() or self._x - 1
             <= ship.get_start_coords()[0] <= self._x + self._length) or self.get_tp() == 2 and ship.get_tp() == 2 and \
            self._x - 1 <= ship.get_start_coords()[0] <= self._x + 1 and \
            (ship.get_start_coords()[1] - 1 <= self._y <= ship.get_start_coords()[1] + ship.get_length() or self._y - 1
             <= ship.get_start_coords()[1] <= self._y + self._length)

    def is_out_pole(self, size):
        if self._tp == 1:
            return not (0 <= self._x < size and 0 <= self._x + self._length - 1 < size and 0 <= self._y < size)
        else:
            return not (0 <= self._y < size and 0 <= self._y + self._length - 1 < size and 0 <= self._x < size)

    def __getitem__(self, item):
        return self._cells[item]

    def __setitem__(self, key, value):
        self._cells[key] = value


class GamePole:
    def __init__(self, size):
        self._size = size
        self._ships = []
        self._pole = []

    def init(self):
        self._ships = [Ship(4, tp=randint(1, 2))] + [Ship(3, tp=randint(1, 2)) for _ in range(2)] \
            + [Ship(2, randint(1, 2)) for _ in range(3)] + [Ship(1, randint(1, 2)) for _ in range(4)]
        self._pole = [[0 for _ in range(self._size)] for _ in range(self._size)]
        k = 0
        while k < len(self._ships):
            x = randint(0, self._size - 1)
            y = randint(0, self._size - 1)
            self._ships[k].set_start_coords(x, y)
            if not any(map(lambda s: (self._ships[k].is_collide(s) if self._ships[k] != s else False) or
                       self._ships[k].is_out_pole(self._size), self._ships)):
                for i in range(self._ships[k].get_length()):
                    if self._ships[k].get_tp() == 1:
                        self._pole[x + i][y] = 1
                    else:
                        self._pole[x][y + i] = 1
                k += 1

    def get_ships(self):
        return self._ships

    def move_ships(self):
        for ship in self._ships:
            go = choice([-1, 1])
            ship.move(go)
            if any(map(lambda s: (ship.is_collide(s) if ship != s else False) or ship.is_out_pole(self._size),
                       self._ships)):
                go = -go
                ship.move(2 * go)
                if any(map(lambda s: (ship.is_collide(s) if ship != s else False) or ship.is_out_pole(self._size),
                           self._ships)):
                    ship.move(-go)
                    go = 0
            if ship.is_ship_move():
                if go < 0:
                    if ship.get_tp() == 1:
                        self._pole[ship.get_start_coords()[0]][ship.get_start_coords()[1]] = 1
                        self._pole[ship.get_start_coords()[0] + ship.get_length()][ship.get_start_coords()[1]] = 0
                    else:
                        self._pole[ship.get_start_coords()[0]][ship.get_start_coords()[1]] = 1
                        self._pole[ship.get_start_coords()[0]][ship.get_start_coords()[1] + ship.get_length()] = 0
                elif go > 0:
                    if ship.get_tp() == 1:
                        self._pole[ship.get_start_coords()[0] - 1][ship.get_start_coords()[1]] = 0
                        self._pole[ship.get_start_coords()[0] + ship.get_length() - 1][ship.get_start_coords()[1]] = 1
                    else:
                        self._pole[ship.get_start_coords()[0]][ship.get_start_coords()[1] - 1] = 0
                        self._pole[ship.get_start_coords()[0]][ship.get_start_coords()[1] + ship.get_length() - 1] = 1

    def show(self):
        [print(*row) for row in self._pole]

    def get_pole(self):
        return tuple([tuple(i) for i in self._pole])

    def set_ship_cell(self, x, y):
        for ship in self._ships:
            for i in range(ship.get_length()):
                if ship.get_tp() == 1:
                    if ship.get_start_coords()[0] + i == x and ship.get_start_coords()[1] == y:
                        ship[i] = 2
                        ship.hit_ship()
                else:
                    if ship.get_start_coords()[1] + i == y and ship.get_start_coords()[0] == x:
                        ship[i] = 2
                        ship.hit_ship()

    def is_ship_killed(self, x, y):
        ship = self.get_ship_by_coords(x, y)
        return all(map(lambda c: c == 2, ship.get_cells()))

    def get_ship_by_coords(self, x, y):
        for ship in self._ships:
            for i in range(ship.get_length()):
                if ship.get_tp() == 1:
                    if ship.get_start_coords()[0] + i == x and ship.get_start_coords()[1] == y:
                        return ship
                else:
                    if ship.get_start_coords()[1] + i == y and ship.get_start_coords()[0] == x:
                        return ship

    def isolate_killed_ship(self, x, y):
        ship = self.get_ship_by_coords(x, y)
        if ship.get_tp() == 1:
            for i in range(ship.get_start_coords()[1] - 1, ship.get_start_coords()[1] + 2):
                for j in range(ship.get_start_coords()[0] - 1, ship.get_start_coords()[0] + ship.get_length() + 1):
                    if 0 <= i < self._size and 0 <= j < self._size and self[j, i] != 2:
                        self[j, i] = '*'
        else:
            for i in range(ship.get_start_coords()[0] - 1, ship.get_start_coords()[0] + 2):
                for j in range(ship.get_start_coords()[1] - 1, ship.get_start_coords()[1] + ship.get_length() + 1):
                    if 0 <= i < self._size and 0 <= j < self._size and self[i, j] != 2:
                        self[i, j] = '*'

    def __getitem__(self, item):
        return self._pole[item[0]][item[1]]

    def __setitem__(self, key, value):
        self._pole[key[0]][key[1]] = value


class SeaBattle:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, is_human_goes_first=True, size=10):
        self.is_human_goes = is_human_goes_first
        self.size = size
        self.human_pole = GamePole(10)
        self.computer_pole = GamePole(10)

    def show_computer_pole(self):
        for i in range(self.size):
            for j in range(self.size):
                if self.computer_pole[i, j] in (0, 1):
                    print('#', end=' ')
                else:
                    print(self.computer_pole[i, j], end=' ')
            print()

    def human_goes(self):
        x, y = map(int, input('Ваш ход: ').split())
        if self.computer_pole[x, y] == 1:
            self.computer_pole.set_ship_cell(x, y)
            self.computer_pole[x, y] = 2
            if self.computer_pole.is_ship_killed(x, y):
                self.computer_pole.isolate_killed_ship(x, y)
                print('Вражеский корабль уничтожен!\n')
            else:
                print('Вражеский корабль подбит!\n')
            self.show_computer_pole()
            print()
        elif self.computer_pole[x, y] == 0:
            self.computer_pole[x, y] = '*'
            print('Промах!\n')
            self.computer_pole.move_ships()
            self.show_computer_pole()
            print()
            self.is_human_goes = False
        else:
            print('эта клетка уже простреляна\n')

    def computer_goes(self):
        x = randint(0, self.size - 1)
        y = randint(0, self.size - 1)
        if self.human_pole[x, y] == 1:
            print(f'Ход соперника: {x} {y}')
            self.human_pole.set_ship_cell(x, y)
            self.human_pole[x, y] = 2
            if self.human_pole.is_ship_killed(x, y):
                self.human_pole.isolate_killed_ship(x, y)
                print('Ваш корабль уничтожен!\n')
            else:
                print('Ваш корабль подбит!\n')
            self.human_pole.show()
            print()
        elif self.human_pole[x, y] == 0:
            print(f'Ход соперника: {x} {y}')
            self.human_pole[x, y] = '*'
            print('Промах!\n')
            self.human_pole.move_ships()
            self.human_pole.show()
            print()
            self.is_human_goes = True

    def start_game(self):
        is_any_ships = True
        self.human_pole.init()
        self.computer_pole.init()
        while is_any_ships:
            if self.is_human_goes:
                self.human_goes()
                is_any_ships = False
                for i in range(self.size):
                    for j in range(self.size):
                        if self.computer_pole[i, j] == 1:
                            is_any_ships = True
                if not is_any_ships:
                    print('Ты выиграл!')
                    break
            else:
                self.computer_goes()
                is_any_ships = False
                for i in range(self.size):
                    for j in range(self.size):
                        if self.human_pole[i, j] == 1:
                            is_any_ships = True
                if not is_any_ships:
                    print('Ты просрал!')
                    break
