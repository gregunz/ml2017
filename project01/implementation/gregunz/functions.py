# -*- coding: utf-8 -*-
"""
Helper Functions
"""

import numpy as np

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def inv_log(x):
    return 1 / (1 + np.log(x))

def abs_sub(x, y):
    return np.abs(x - y)

def mult(x, y, deg=1):
    return x**deg * y**deg