# coding:utf-8
__author__ = 'XingHua'

"""
光栅尺位置VS出光学位置
参考点为d1前面的那个镜子，见90nm的ZA图纸。
从Excel中的光栅尺位置计算出光学位置d1,d2,d3,d5.
从光学位置计算出光栅尺位置。
"""

import matplotlib.pyplot as plt
import numpy as np
from glob import glob
import pandas as pd
import argparse
import sys
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


print(quadratic(2, 3, 1))
print(quadratic(1, 3, -4))
