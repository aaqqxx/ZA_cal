# coding:utf-8
# !/usr/env/bin/python

__author__ = 'aaqqxx'

"""
用来计算ZA各个镜片间距。
"""

import numpy as np
from scipy.integrate import quad, dblquad, nquad
import matplotlib.pyplot as plt
from scipy.linalg import solve
from sympy import Symbol
import sympy
import re

IL_mode_dict = {
    "ZA_CONVERT_MATRIX_CONVENTIONNAL_SMALLSIGMA": [],
    "ZA_CONVERT_MATRIX_CONVENTIONNAL_BIGSIGMA": [],
    "ZA_CONVERT_MATRIX_ANNULAR_BIGSIGMA": [],
    "ZA_CONVERT_MATRIX_ANNULAR_SMALLSIGMA": [],
    "ZA_CONVERT_MATRIX_DIPOLE_QUADRUPOLE_SMALLSIGMA_SMALLSIGMAOUT": [],
    "ZA_CONVERT_MATRIX_DIPOLE_QUADRUPOLE_SMALLSIGMA_BIGSIGMAOUT": [],
    "ZA_CONVERT_MATRIX_DIPOLE_QUADRUPOLE_BIGSIGMA": [],
    "ZA_CONVERT_MATRIX_DIPOLE_X_SMALLSIGMA_SMALLSIGMAOUT": [],
    "ZA_CONVERT_MATRIX_DIPOLE_X_SMALLSIGMA_BIGSIGMAOUT": [],
    "ZA_CONVERT_MATRIX_DIPOLE_X_BIGSIGMA": [],
    "ZA_CONVERT_MATRIX_DIPOLE_Y_SMALLSIGMA_SMALLSIGMAOUT": [],
    "ZA_CONVERT_MATRIX_DIPOLE_Y_SMALLSIGMA_BIGSIGMAOUT": [],
    "ZA_CONVERT_MATRIX_DIPOLE_Y_BIGSIGMA": [],

}


def cal_distance(IL_mode, sigma_out, sigma_in, NA=0.75):
    pass


def get_distance_form_file(file_name):
    pass


import math
def quadratic(a, b, c):
    if not isinstance(a, (int, float)):
        raise TypeError('a is not a number')
    if not isinstance(b, (int, float)):
        raise TypeError('b is not a number')
    if not isinstance(c, (int, float)):
        raise TypeError('c is not a number')
    derta = b * b - 4 * a * c
    if a == 0:
        if b == 0:
            if c == 0:
                return '方程根是全体实数'
            else:
               return '方程无根'
        else:
            x1 = -c / b
            x2 = x1
            return x1, x2
    else:
        if derta < 0:
            return '方程无根'
        else:
            x1 = (-b + math.sqrt(derta)) / (2 * a)
            x2 = (-b - math.sqrt(derta)) / (2 * a)
            return x1, x2


if __name__ == '__main__':
    filename = "doc/IL4_za_transfer_matrix20171017.ini"
    txt = open(filename).read()
    res = re.findall("\[(Z.+)\]", txt)
    for each in res:
        print(each)
    # print(res)
    print(quadratic(1, -2, 1))
    print(quadratic(1, 3, -4))
    print(quadratic(0.5352, 3.7357, -0.30977314))
    pass
