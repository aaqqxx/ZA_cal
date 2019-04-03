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

# unit:mm
z1_optical_home_pos = 150.433
z2_optical_home_pos = 263.01
z3_optical_home_pos = 338.513
z4_optical_home_pos = 87  # Axicon

factor = 1000  # m2mm


def get_d1_d2_d3_d5(z1_ruler, z2_ruler, z3_ruler, z4_ruler):
    """
    通过光栅尺位置计算得到光学间距，参考是d1前面那个镜片，见ZA图纸。
    :param z1_ruler: mm
    :param z2_ruler: mm
    :param z3_ruler: mm
    :param z4_ruler: mm
    :return: d1, d2, d3, d5      unit:mm
    """
    d1 = z1_ruler + z1_optical_home_pos
    d2 = z2_ruler + z2_optical_home_pos - d1
    d3 = z3_ruler + z3_optical_home_pos - d1 - d2
    d5 = z4_ruler + z4_optical_home_pos
    return d1, d2, d3, d5
    pass


def get_ruler1_ruler2_ruler3_ruler4(d1, d2, d3, d5):
    """
    通过光学间距计算得到光栅尺位置，参考是d1前面那个镜片，见ZA图纸。
    :param d1: mm
    :param d2: mm
    :param d3: mm
    :param d5: mm
    :return: z1_ruler, z2_ruler, z3_ruler, z4_ruler     unit:mm
    """
    z1_ruler = d1 - z1_optical_home_pos
    z2_ruler = d1 + d2 - z2_optical_home_pos
    z3_ruler = d1 + d2 + d3 - z3_optical_home_pos
    z4_ruler = d5 - z4_optical_home_pos
    return np.array([z1_ruler, z2_ruler, z3_ruler, z4_ruler])
    pass


def ann_excel_get_ruler_pos():
    if len(sys.argv) > 2:
        filename = sys.argv[1]
        print filename
    else:
        print "Please write the excel file path"
        # exit()
        filename = u"doc/20181204 90nm光刻机光瞳测试数据整理--朱思羽[2450].xlsx"
    data = pd.read_excel(filename, skiprows=2)
    # print data.ix[0][2:6]
    for index in data.index:
        ruler_pos = data.ix[index][2:6] * factor
        # print ruler_pos
        print get_d1_d2_d3_d5(ruler_pos[0], ruler_pos[1], ruler_pos[2], ruler_pos[3])
    pass


if __name__ == "__main__":
    # parser = argparse.ArgumentParser(description='Process excel data to get d1,d2,d3,d5.')
    # parser.add_argument('filename', choices=['filename'], type=str,
    #                     help='a excel file for the calc')

    # args = parser.parse_args()
    # print(args.accumulate(args.filename))
    # print "dsssssssssssss"
    # ann_excel_get_ruler_pos()
    print get_ruler1_ruler2_ruler3_ruler4(141.743, 81.771, 74.276, 5)/1000.
