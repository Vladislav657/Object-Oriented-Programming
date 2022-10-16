class Vertex:
    def __init__(self):
        self._links = []

    def get_links(self):
        return self._links

    links = property(get_links)


class Link:
    def __init__(self, v1, v2):
        self._v1, self._v2 = v1, v2
        self._v1.links.append(self)
        self._v2.links.append(self)
        self._dist = 1

    def get_v1(self):
        return self._v1

    def get_v2(self):
        return self._v2

    def get_dist(self):
        return self._dist

    def set_dist(self, dist):
        self._dist = dist

    v1, v2 = property(get_v1), property(get_v2)
    dist = property(get_dist, set_dist)


class LinkedGraph:
    def __init__(self):
        self._links = []
        self._vertex = []

    def add_vertex(self, v):
        if v not in self._vertex:
            self._vertex.append(v)

    def add_link(self, link):
        if not len(list(filter(lambda o: o.v1 == link.v1 and o.v2 == link.v2 or o.v1 == link.v2 and o.v2 == link.v1,
                        self._links))):
            self._links.append(link)
            if link.v1 not in self._vertex:
                self._vertex.append(link.v1)
            if link.v2 not in self._vertex:
                self._vertex.append(link.v2)

    def get_link(self, v1, v2):
        for link in self._links:
            if v1 == link.v1 and v2 == link.v2 or v1 == link.v2 and v2 == link.v1:
                return link

    def find_path(self, start_v, stop_v):
        graph = {v: [link.v1 if link.v1 != v else link.v2 for link in v.links if v in (link.v1, link.v2)] for v in
                 self._vertex}
        path_lengths = {v: 0 if v == start_v else None for v in self._vertex}

        def set_lengths(v):
            nonlocal graph, path_lengths
            for i in graph[v]:
                if path_lengths[i] is None or path_lengths[v] + self.get_link(v, i).dist < path_lengths[i]:
                    path_lengths[i] = path_lengths[v] + self.get_link(v, i).dist
                    set_lengths(i)

        def get_path(v, path, links):
            nonlocal graph, path_lengths
            if v != start_v:
                vertex = [i for i in graph[v] if path_lengths[v] - self.get_link(v, i).dist == path_lengths[i]]
                path.append(min(vertex, key=lambda x: path_lengths[x]))
                links.append(self.get_link(v, min(vertex, key=lambda x: path_lengths[x])))
                get_path(min(vertex, key=lambda x: path_lengths[x]), path, links)
            return path[::-1], links[::-1]

        set_lengths(start_v)
        return get_path(stop_v, [stop_v], [])


class Station(Vertex):
    def __init__(self, name):
        super(Station, self).__init__()
        self.name = name

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name


class LinkMetro(Link):
    def __init__(self, v1, v2, dist):
        super(LinkMetro, self).__init__(v1, v2)
        self.dist = dist
