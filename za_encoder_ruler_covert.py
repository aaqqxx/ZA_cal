# coding:utf-8
__author__ = 'XingHua'

"""
文件描述
"""

import math
import numpy as np
import matplotlib.pyplot as plt

if __name__ == '__main__':
    filename_p = "tuning_data/encoder_ruler_covert.txt"
    filename_n = "tuning_data/encoder_ruler_covert_n.txt"
    data_all_p = np.loadtxt(filename_p, skiprows=1, unpack=True)
    data_all_n = np.loadtxt(filename_n, skiprows=1, unpack=True)

    # plt.plot(a, "-o", label="encoder")
    # plt.plot(-b, "-o", label="ruler1")
    # plt.plot(-c, "-o", label="ruler2")
    # plt.plot(-d, "-o", label="ruler3")
    # plt.plot(-mean, "-o", label="ruler_mean")
    a = [0, 1, 2, 3]
    b = [2, 3, 45, 6]
    # plt.plot(a, b, "-o", label="ruler")
    plt.plot(data_all_p[2], data_all_p[1], "-o", label="ruler_p")
    # plt.plot(data_all_n[2], data_all_n[1], "-o", label="ruler_n")
    # plt.plot(data_all[2], "-o", label="encoder")
    plt.legend()
    plt.show()
