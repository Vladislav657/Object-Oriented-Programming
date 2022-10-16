def get_z(obj):
    try:
        return obj.z
    except AttributeError:
        print("Атрибут с именем z не существует")


def is_convertable(n):
    try:
        int(n)
        return True
    except ValueError:
        return False


def convert_to_num(n):
    try:
        return int(n)
    except ValueError:
        try:
            return float(n)
        except ValueError:
            return n


class Triangle:
    def __init__(self, a, b, c):
        if type(a) not in (float, int) or a <= 0 or type(b) not in (float, int) or b <= 0 or type(c) \
                not in (float, int) or c <= 0:
            raise TypeError('стороны треугольника должны быть положительными числами')
        if not (a + b > c and a + c > b and b + c > a):
            raise ValueError('из указанных длин сторон нельзя составить треугольник')
        self._a, self._b, self._c = a, b, c


def is_triangle(t):
    try:
        Triangle(*t)
        return True
    except (TypeError, ValueError):
        return False


class FloatValidator:
    def __init__(self, min_value, max_value):
        self.min_value = min_value
        self.max_value = max_value

    def __call__(self, *args, **kwargs):
        if not (type(args[0]) is float and self.min_value <= args[0] <= self.max_value):
            raise ValueError('значение не прошло валидацию')


class IntegerValidator:
    def __init__(self, min_value, max_value):
        self.min_value = min_value
        self.max_value = max_value

    def __call__(self, *args, **kwargs):
        if not (type(args[0]) is int and self.min_value <= args[0] <= self.max_value):
            raise ValueError('значение не прошло валидацию')


def is_valid(lst, validators):
    new_lst = []
    for n in lst:
        for v in validators:
            try:
                v(n)
                new_lst.append(n)
                break
            except ValueError:
                continue
    return new_lst


def add_values(value1, value2):
    try:
        return int(value1) + int(value2)
    except ValueError:
        try:
            return float(value1) + float(value2)
        except ValueError:
            return value1 + value2


class Point:
    def __init__(self, x=0.0, y=0.0):
        self._x, self._y = x, y


def set_point(x, y):
    try:
        return Point(int(x), int(y))
    except ValueError:
        try:
            return Point(float(x), float(y))
        except ValueError:
            return Point()


def get_loss(w1, w2, w3, w4):
    try:
        res = 10 * w1 // w2
    except ZeroDivisionError:
        return "деление на ноль"
    else:
        return res - 5 * w2 * w3 + w4


class Rect:
    def __init__(self, x, y, width, height):
        if type(x) not in (float, int) or type(y) not in (float, int) or \
                type(width) not in (float, int) or width <= 0 or type(height) not in (float, int) or height <= 0:
            raise ValueError('некорректные координаты и параметры прямоугольника')
        self._x, self._y = x, y
        self._width = width
        self._height = height

    def get_x(self):
        return self._x

    def get_y(self):
        return self._y

    def get_width(self):
        return self._width

    def get_height(self):
        return self._height

    def is_collision(self, rect):
        if self._y < rect.get_y() - rect.get_height() or self._y - self._height > rect.get_y() or \
                self._x > rect.get_x() + rect.get_width() or self._x + self._width < rect.get_x():
            return True
        raise TypeError('прямоугольники пересекаются')


def not_collision(rect1, rect2):
    try:
        return rect1.is_collision(rect2) if rect1 != rect2 else True
    except TypeError:
        return False
