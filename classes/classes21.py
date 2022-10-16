def input_int_numbers():
    try:
        s = tuple(map(int, input().split()))
    except ValueError:
        raise TypeError('все числа должны быть целыми')
    else:
        return s


class ValidatorString:
    def __init__(self, min_length, max_length, chars):
        self.min_length = min_length
        self.max_length = max_length
        self.chars = chars

    def is_valid(self, string):
        if self.min_length <= len(string) <= self.max_length and \
                (len(self.chars) == 0 or any(map(lambda c: c in string, self.chars))):
            return True
        raise ValueError('недопустимая строка')


class LoginForm:
    def __init__(self, login_validator, password_validator):
        self._login, self._password = None, None
        self.login_validator = login_validator
        self.password_validator = password_validator

    def form(self, request):
        if 'login' not in request or 'password' not in request:
            raise TypeError('в запросе отсутствует логин или пароль')
        if self.login_validator.is_valid(request['login']) and self.password_validator.is_valid(request['password']):
            self._login, self._password = request['login'], request['password']


class Test:
    def __init__(self, descr):
        if not 10 <= len(descr) <= 10000:
            raise ValueError('формулировка теста должна быть от 10 до 10 000 символов')
        self.descr = descr

    def run(self):
        raise NotImplementedError


class TestAnsDigit(Test):
    def __init__(self, descr, ans_digit, max_error_digit=0.01):
        super(TestAnsDigit, self).__init__(descr)
        if not (type(ans_digit) in (int, float) and type(max_error_digit) in (int, float) and max_error_digit >= 0):
            raise ValueError('недопустимые значения аргументов теста')
        self.ans_digit = ans_digit
        self.max_error_digit = max_error_digit

    def run(self):
        ans = float(input())
        return self.ans_digit - self.max_error_digit <= ans <= self.ans_digit + self.max_error_digit


class TupleLimit(tuple):
    def __new__(cls, *args, **kwargs):
        return super(TupleLimit, cls).__new__(cls)

    def __init__(self, lst, max_length):
        if len(lst) > max_length:
            raise ValueError('число элементов коллекции превышает заданный предел')
        self.lst = lst

    def __str__(self):
        return ' '.join(list(map(str, self.lst)))

    def __repr__(self):
        return ' '.join(list(map(str, self.lst)))


class StringException(Exception):
    __doc__ = '''StringException'''


class NegativeLengthString(StringException):
    __doc__ = '''NegativeLengthString'''


class ExceedLengthString(StringException):
    __doc__ = '''ExceedLengthString'''


class PrimaryKeyError(Exception):
    def __init__(self, **kwargs):
        if len(list(kwargs.keys())) == 0:
            self.message = "Первичный ключ должен быть целым неотрицательным числом"
        else:
            self.message = f"Значение первичного ключа {list(kwargs.keys())[0]} = {list(kwargs.values())[0]} " \
                           f"недопустимо"

    def __str__(self):
        return self.message


class DateString:
    def __init__(self, date_string):
        if not (len(date_string.split('.')) == 3 and 1 <= int(date_string.split('.')[0]) <= 31 and 1 <=
                int(date_string.split('.')[1]) <= 12 and 1 <= int(date_string.split('.')[2]) <= 3000):
            raise DateError
        self.date_string = date_string

    def __str__(self):
        return '.'.join([self.date_string.split('.')[0].rjust(2, '0'), self.date_string.split('.')[1].rjust(2, '0'),
                        self.date_string.split('.')[2].rjust(4, '0')])


class DateError(Exception):
    __doc__ = '''DateError'''
