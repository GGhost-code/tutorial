class Graph():
    def __init__(self, matrix=None, dct=None, size=None) -> None:
        if matrix is not None:
            self.matrix = matrix
            self.dct = self._make_dict(matrix)
        elif dct is not None:
            self.dct = dct
            self.matrix = self._make_matrix(dct, size)
        else:
            raise RuntimeError("no graph")

    def _make_dict(self, matrix):
        d = dict()
        for i in range(1, len(matrix) + 1):
            d[i] = []
            for j in range(1, len(matrix[i - 1]) + 1):
                if matrix[i - 1][j- 1] == 1:
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

    def count_edges(self):
        c = 0
        for i in self.matrix:
            for j in i:
                if j == 1:
                    c += 1
        c //= 2
        return c

    def has_path(self, start, end):
        pass

    def shortest_path(self, start, end):
        pass

    def is_connective(self):
        pass

size = int(input())
matrix = [list(map(int, input().split())) for i in range(size)]
g = Graph(size=size, matrix=matrix)
print(g.count_edges())