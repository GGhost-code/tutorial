class Graph:
    def __init__(self, matrix=None, dct=None, list_of_edges=None, size=None) -> None:
        self.small_visited = None
        self.visited = None
        if matrix is not None:
            self.matrix = matrix
            self.dct = self._make_dict(matrix)
        elif dct is not None:
            self.dct = dct
            self.matrix = self._make_matrix(dct, size)
        elif list_of_edges is not None:
            self.dct = self._make_dct_of_loe(list_of_edges, size)
            self.matrix = self._make_matrix(self.dct, size)
        else:
            raise RuntimeError("no graph")
        self.size = len(self.matrix) if size is None else size

    def print_matrix(self):
        for i in self.matrix:
            print(" ".join(map(str, i)))

    def _make_dict(self, matrix):
        d = dict()
        for i in range(1, len(matrix) + 1):
            d[i] = []
            for j in range(1, len(matrix[i - 1]) + 1):
                if matrix[i - 1][j - 1] == 1:
                    d[i].append(j)
        return d

    def _make_matrix(self, dict, size):
        m = []
        for i in range(1, len(dict) + 1):
            m.append([])
            for j in range(1, size + 1):
                if j in dict[i]:
                    m[i - 1].append(1)
                else:
                    m[i - 1].append(0)
        return m

    def _make_dct_of_loe(self, list_of_edges, size):
        d = dict()
        for i in range(1, size + 1):
            d[i] = []
        for i in list_of_edges:
            d[i[0]].append(i[1])
            d[i[1]].append(i[0])
        return d

    def count_edges(self):
        c = 0
        for i in self.matrix:
            for j in i:
                if j == 1:
                    c += 1
        c //= 2
        return c

    def dfs(self, started):
        visited = set()
        visited.add(started)
        self._dfs(visited, started)
        self.visited = visited

    def _dfs(self, visited, started):
        for v in self.dct[started]:
            if v in visited:
                pass
            else:
                visited.add(v)
                self._dfs(visited, v)

    def pathes_count(self, v):
        self.dfs(v)
        print(len(self.visited))

    def connectivity_components_count(self):
        self.visited = set()
        self.small_visited = set()
        lot = []

        c = 0
        for i in range(1, self.size + 1):
            if i not in self.visited:
                self.small_visited = set()
                self.small_visited.add(i)
                self._dfs(self.small_visited, i)
                for j in self.small_visited:
                    self.visited.add(j)
                # self.visited = self.visited.union(self.small_visited)
                lot.append((len(self.small_visited), list(self.small_visited)))
                c += 1
            if len(self.visited) == self.size:
                break
        print(c)
        for i in lot:
            print(i[0])
            print(" ".join(map(str, i[1])))

    def has_path(self, start, end):
        pass

    def shortest_path(self, start, end):
        pass

    def is_connective(self):
        pass


a = list(map(int, input().split()))
v = a[1]
size = a[0]
loe = [list(map(int, input().split())) for i in range(v)]
# matrix = [list(map(int, input().split())) for i in range(size)]
g = Graph(size=size, list_of_edges=loe)
g.connectivity_components_count()
