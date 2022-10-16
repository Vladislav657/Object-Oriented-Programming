class Animal:
    def __init__(self, name, old):
        self.name = name
        self.old = old


class Cat(Animal):
    def __init__(self, name, old, color, weight):
        super().__init__(name, old)
        self.color = color
        self.weight = weight

    def get_info(self):
        return f"{self.name}: {self.old}, {self.color}, {self.weight}"


class Dog(Animal):
    def __init__(self, name, old, breed, size):
        super().__init__(name, old)
        self.breed = breed
        self.size = size

    def get_info(self):
        return f"{self.name}: {self.old}, {self.breed}, {self.size}"


class Thing:
    id = 0

    def __init__(self, name, price, weight=None, dims=None, memory=None, frm=None):
        self.id = Thing.id
        self.name = name
        self.price = price
        self.weight = weight
        self.dims = dims
        self.memory = memory
        self.frm = frm
        Thing.id += 1

    def get_data(self):
        return self.id, self.name, self.price, self.weight, self.dims, self.memory, self.frm


class Table(Thing):
    def __init__(self, name, price, weight, dims):
        super().__init__(name, price, weight=weight, dims=dims)


class ElBook(Thing):
    def __init__(self, name, price, memory, frm):
        super().__init__(name, price, memory=memory, frm=frm)


class GenericView:
    def __init__(self, methods=('GET',)):
        self.methods = methods

    def get(self, request):
        pass

    def post(self, request):
        pass

    def put(self, request):
        pass

    def delete(self, request):
        pass


class DetailView(GenericView):
    def __init__(self, methods=('GET',)):
        super().__init__(methods)

    def render_request(self, request, method):
        if method not in self.methods:
            raise TypeError('данный запрос не может быть выполнен')
        return self.get(request)

    def get(self, request):
        if type(request) != dict:
            raise TypeError('request не является словарем')
        if 'url' not in request:
            raise TypeError('request не содержит обязательного ключа url')
        return f"url: {request['url']}"


class Singleton:
    __instance = None
    __name = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self, name):
        if Singleton.__name is None:
            Singleton.__name = name
        self.name = Singleton.__name


class Game(Singleton):
    def __init__(self, name):
        super().__init__(name)


class Validator:
    @staticmethod
    def _is_valid(data):
        return bool(data)

    def __call__(self, *args, **kwargs):
        if not self._is_valid(args[0]):
            raise ValueError('данные не прошли валидацию')


class IntegerValidator(Validator):
    def __init__(self, min_value, max_value):
        self.min_value = min_value
        self.max_value = max_value

    def _is_valid(self, data):
        return type(data) is int and self.min_value <= data <= self.max_value


class FloatValidator(Validator):
    def __init__(self, min_value, max_value):
        self.min_value = min_value
        self.max_value = max_value

    def _is_valid(self, data):
        return type(data) is float and self.min_value <= data <= self.max_value


class Layer:
    def __init__(self):
        self.name = 'Layer'
        self.next_layer = None

    def __call__(self, *args, **kwargs):
        self.next_layer = args[0]
        return args[0]


class Input(Layer):
    def __init__(self, inputs):
        super().__init__()
        self.name = 'Input'
        self.inputs = inputs


class Dense(Layer):
    def __init__(self, inputs, outputs, activation):
        super().__init__()
        self.name = 'Dense'
        self.inputs = inputs
        self.outputs = outputs
        self.activation = activation


class NetworkIterator:
    def __init__(self, layer):
        self.layer = layer

    def __iter__(self):
        self.value = Layer()
        self.value(self.layer)
        return self

    def __next__(self):
        if self.value.next_layer is not None:
            self.value = self.value.next_layer
        else:
            raise StopIteration
        return self.value


class Vector:
    def __init__(self, *args):
        self.coords = args

    def __add__(self, other):
        if len(self.coords) != len(other.coords):
            raise TypeError('размерности векторов не совпадают')
        return Vector(*[self.coords[i] + other.coords[i] for i in range(len(self.coords))])

    def __sub__(self, other):
        if len(self.coords) != len(other.coords):
            raise TypeError('размерности векторов не совпадают')
        return Vector(*[self.coords[i] - other.coords[i] for i in range(len(self.coords))])

    def get_coords(self):
        return self.coords


class VectorInt(Vector):
    def __init__(self, *args):
        for i in args:
            if type(i) != int:
                raise ValueError('координаты должны быть целыми числами')
        super().__init__(*args)

    def __add__(self, other):
        if len(self.coords) != len(other.coords):
            raise TypeError('размерности векторов не совпадают')
        new_coords = [self.coords[i] + other.coords[i] for i in range(len(self.coords))]
        for i in new_coords:
            if type(i) is float:
                return Vector(*new_coords)
        return VectorInt(*new_coords)

    def __sub__(self, other):
        if len(self.coords) != len(other.coords):
            raise TypeError('размерности векторов не совпадают')
        new_coords = [self.coords[i] - other.coords[i] for i in range(len(self.coords))]
        for i in new_coords:
            if type(i) is float:
                return Vector(*new_coords)
        return VectorInt(*new_coords)
