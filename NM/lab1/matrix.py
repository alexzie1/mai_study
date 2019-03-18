import copy
import json


class Vector:
    def __init__(self, sz=None):
        if sz is not None:
            self.data = [0] * sz
        else:
            self.data = []

    def __getitem__(self, idx):
        return self.data[idx]

    def __setitem__(self, idx, item):
        if idx >= len(self):
            self.data.extend(idx + 1)
        self.data[idx] = item

    def __len__(self):
        return len(self.data)

    def __str__(self):
        res = '\n'
        for i in self:
            res += '{0}\n'.format(i)
        return res

    def append(self, item):
        self.data.append(item)

    def get_data(self):
        return self.data


class Matrix:
    def __init__(self, orig=None):
        if orig is None:
            self.non_copy_constructor()
        else:
            self.copy_constructor(orig)

    def non_copy_constructor(self):
        self.size = 0
        self.data = []

    def copy_constructor(self, orig):
        self.size = orig.size
        self.data = copy.deepcopy(orig.data)

    def __getitem__(self, idx):
        return self.data[idx]

    def __setitem__(self, idx, item):
        if idx >= len(self):
            self.data.extend(idx + 1)
        self.data[idx] = item

    def __len__(self):
        return len(self.data)

    def __str__(self):
        res = '\n'
        for i in range(self.size):
            for j in range(self.size):
                res += str(self.data[i][j]) + ' '
            res += '\n'
        return res

    def get_data(self):
        return self.data

    def multiply(self, other):
        other_T = list(zip(*other))
        result = Matrix.from_list([[sum(ea * eb for ea, eb in zip(a, b)) for b in other_T] for a in self])
        return result

    def debug_print(self):
        for i in self.data:
            print(*i)

    def transpose(self):
        self.data = [list(i) for i in zip(*self.data)]

    @classmethod
    def _make_matrix(cls, rows):
        mat = Matrix()
        mat.size = len(rows)
        mat.data = rows
        return mat

    @classmethod
    def zero(cls, sz):
        obj = Matrix()
        obj.size = sz
        obj.data = [[0] * sz for _ in range(sz)]
        return obj

    @classmethod
    def identity(cls, sz):
        obj = Matrix()
        obj.size = sz
        obj.data = [[1 if i == j else 0 for j in range(sz)] for i in range(sz)]
        return obj

    @classmethod
    def from_list(cls, list_of_lists):
        rows = list_of_lists[:]
        return cls._make_matrix(rows)


class TridiagonalMatrix:
    def __init__(self):
        self.size = 0
        self.a = []
        self.b = []
        self.c = []

    def __len__(self):
        return len(self.b)

    def __str__(self):
        res = '\n'
        res += str(self.b[0]) + ' ' + str(self.c[0]) + '\n'
        for i in range(1, len(self) - 1):
            res += str(self.a[i]) + ' ' + str(self.b[i]) + ' ' + str(self.c[i]) + '\n'
        res += str(self.a[-1]) + ' ' + str(self.b[-1]) +'\n'
        return res

    def debug_print(self, D):
        for i in range(self.size):
            print("{0} {1} {2} {3}".format(self.a[i], 
                self.b[i], self.c[i], D[i]))