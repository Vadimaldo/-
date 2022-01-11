import numpy as np


def make_vec(a, b):
    t = []
    for c1, c2 in zip(a, b):
        t.append(c2 - c1)
    return np.array(t)


def vec_len(v):
    return np.sqrt(v.dot(v))


def scalar_mult(v1, v2):
    return np.dot(v1, v2)


def cos_of_vect_angle(v1, v2):
    return np.sum(v1 * v2) / (vec_len(v1) * vec_len(v2))


def vec_project(v1, v2):
    cos_ratio = cos_of_vect_angle(v1, v2)
    len_ratio = vec_len(v1) / vec_len(v2)
    return v2 * len_ratio * cos_ratio


def dot_project(v1, v2, v_start):
    return vec_project(v1, v2) + v_start


def vect_mult(v1, v2):
    return np.cross(v1, v2)


def triple_product(v1, v2, v3):
    return v1 * np.cross(v2, v3)


def piramid_space(v1, v2, v3):
    return vec_len(triple_product(v1, v2, v3)) / 2


def triangle_area(v1, v2):
    return vec_len(vect_mult(v1, v2)) / 2


class Plane():

    def __init__(self, dot, v, w):
        self.A = v[1] * w[2] - v[2] * w[1]
        self.B = v[2] * w[0] - v[0] * w[2]
        self.C = v[0] * w[1] - v[1] * w[0]
        self.D = dot[0] * (v[2] * w[1] - v[1] * w[2]) + dot[1] * (v[0] * w[2] - v[2] * w[0]) + dot[2] * (v[1] * w[0] - v[0] * w[1])

    def _add_to_equation(self, eq, k, var=''):
        if k != 0:
            if eq != '':
                eq += ' + '
            if k != 1 or var == '':
                eq += f'{k}{var}'
            else:
                eq += f'{var}'
        return eq

    def equation(self):
        eq = ''

        eq = self._add_to_equation(eq, self.A, 'x')
        eq = self._add_to_equation(eq, self.B, 'y')
        eq = self._add_to_equation(eq, self.C, 'z')
        eq = self._add_to_equation(eq, self.D)

        return eq + ' = 0'


def plane_cos(p1, p2):
    res = np.absolute(p1.A * p2.A + p1.B * p2.B + p1.C * p2.C)
    res /= np.sqrt(p1.A ** 2 + p1.B ** 2 + p1.C ** 2)
    res /= np.sqrt(p2.A ** 2 + p2.B ** 2 + p2.C ** 2)
    return res


if __name__ == '__main__':
    # set points
    a = [-2, 1, 7]
    b = [1, 4, -2]
    c = [7, 10, -5]
    d = [4, -2, 1]

    # a = [0, 0, 0]
    # b = [1, 0, 0]
    # c = [0, 1, 0]
    # d = [0, 0, 1]

    # create vectors
    ab = make_vec(a, b)
    ac = make_vec(a, c)
    ad = make_vec(a, d)

    ba = make_vec(b, a)
    bc = make_vec(b, c)
    bd = make_vec(b, d)

    ca = make_vec(c, a)
    cb = make_vec(c, b)
    cd = make_vec(c, d)

    # calc
    print('task 1')
    print(f'scalar mult: {scalar_mult(ac, ad)}')
    print(f'cos of ABC: {cos_of_vect_angle(ba, bc)}')
    print()

    print('task 2')
    print(f'vect mult: {vect_mult(ab, cd)}')
    print()

    print('task 3')
    print(f'triple product: {triple_product(ab, ac, ad)}')
    print(f'piramid space: {piramid_space(ab, ac, ad)}')
    print()

    print('task 4')
    print(f'projection of A on BD: {dot_project(ba, bd, b)}')
    print()

    print('task 5')
    ABC = Plane(a, ab, ac)
    ABD = Plane(a, ab, ad)
    print(f'ABC plane: {ABC.equation()}')
    print(f'ABD plane: {ABD.equation()}')
    print(f'ABC and ABD cos: {plane_cos(ABC, ABD)}')
    print()

    print('task 6')
    print(f'area of BCD: {triangle_area(cb, cd)}')
    print()
