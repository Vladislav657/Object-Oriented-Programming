class Digit:
    def __init__(self, value):
        if type(value) not in (int, float):
            raise TypeError('значение не соответствует типу объекта')
        self.value = value


class Integer(Digit):
    def __init__(self, value):
        if type(value) != int:
            raise TypeError('значение не соответствует типу объекта')
        super(Integer, self).__init__(value)


class Float(Digit):
    def __init__(self, value):
        if type(value) != float:
            raise TypeError('значение не соответствует типу объекта')
        super(Float, self).__init__(value)


class Positive(Digit):
    def __init__(self, value):
        if type(value) not in (int, float) or value <= 0:
            raise TypeError('значение не соответствует типу объекта')
        super(Positive, self).__init__(value)


class Negative(Digit):
    def __init__(self, value):
        if type(value) not in (int, float) or value >= 0:
            raise TypeError('значение не соответствует типу объекта')
        super(Negative, self).__init__(value)


class PrimeNumber(Integer, Positive):
    def __init__(self, value):
        super(PrimeNumber, self).__init__(value)


class FloatPositive(Float, Positive):
    def __init__(self, value):
        super(FloatPositive, self).__init__(value)


class ShopItem:
    ID_SHOP_ITEM = 0

    def __init__(self):
        super().__init__()
        ShopItem.ID_SHOP_ITEM += 1
        self._id = ShopItem.ID_SHOP_ITEM

    def get_pk(self):
        return self._id


class ShopGenericView:
    def __str__(self):
        return '\n'.join([i + ': ' + str(self.__dict__[i]) for i in self.__dict__])

    def __repr__(self):
        return '\n'.join([i + ': ' + str(self.__dict__[i]) for i in self.__dict__])


class ShopUserView:
    def __str__(self):
        return '\n'.join([i + ': ' + str(self.__dict__[i]) for i in self.__dict__ if i != '_id'])

    def __repr__(self):
        return '\n'.join([i + ': ' + str(self.__dict__[i]) for i in self.__dict__ if i != '_id'])


class Book(ShopItem, ShopUserView):
    def __init__(self, title, author, year):
        super().__init__()
        self._title = title
        self._author = author
        self._year = year


class RetriveMixin:
    @staticmethod
    def get(request):
        return "GET: " + request.get('url')


class CreateMixin:
    @staticmethod
    def post(request):
        return "POST: " + request.get('url')


class UpdateMixin:
    @staticmethod
    def put(request):
        return "PUT: " + request.get('url')


class GeneralView:
    allowed_methods = ('GET', 'POST', 'PUT', 'DELETE')

    def render_request(self, request):
        if request['method'] not in self.allowed_methods:
            raise TypeError(f"Метод {request.get('method')} не разрешен.")
        method_request = request.get('method').lower()
        return super().__getattribute__(method_request)(request)


class DetailView(RetriveMixin, UpdateMixin, GeneralView):
    allowed_methods = ('GET', 'PUT', )


class Money:
    def __init__(self, value):
        if type(value) not in (float, int):
            raise TypeError('сумма должна быть числом')
        self._money = value

    def get_money(self):
        return self._money

    def set_money(self, value):
        self._money = value

    money = property(get_money, set_money)


class MoneyOperators:
    def __add__(self, other):
        if type(other) in (int, float):
            return self.__class__(self.money + other)

        if type(self) != type(other):
            raise TypeError('Разные типы объектов')

        return self.__class__(self.money + other.money)

    def __sub__(self, other):
        if type(other) in (int, float):
            return self.__class__(self.money - other)

        if type(self) != type(other):
            raise TypeError('Разные типы объектов')

        return self.__class__(self.money - other.money)


class MoneyR(Money, MoneyOperators):
    def __str__(self):
        return f"MoneyR: {self.money}"


class MoneyD(Money, MoneyOperators):
    def __str__(self):
        return f"MoneyD: {self.money}"
