class Server:
    ip = 0
    buffer = []

    def __new__(cls, *args, **kwargs):
        cls.ip += 1
        obj = super().__new__(cls)
        setattr(obj, 'ip', cls.ip)
        setattr(obj, 'buffer', list())
        return obj

    @staticmethod
    def send_data(data):
        Router.buffer.append(data)

    def get_data(self):
        data = self.buffer.copy()
        self.buffer.clear()
        return data

    def get_ip(self):
        return self.ip


class Router:
    buffer = []
    servers = []

    def link(self, server):
        self.servers.append(server)

    def unlink(self, server):
        self.servers.remove(server)

    def send_data(self):
        for i in self.buffer:
            for j in self.servers:
                if j.ip == i.ip:
                    j.buffer.append(i)
        self.buffer.clear()


class Data:
    def __init__(self, data, ip):
        self.data = data
        self.ip = ip
