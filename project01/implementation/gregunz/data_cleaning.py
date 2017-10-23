# -*- coding: utf-8 -*-
"""
Data Cleaning 
"""

import numpy as np        

def replace_invalid(x, mask_invalid, replace_by=None):

    # construct the masked array
    masked_x = np.ma.array(x, mask=mask_invalid)

    # default filled values are zeroes
    fill_value = [0] * x.shape[1]

    # replace with the mean
    if replace_by.lower() == "mean":
        fill_value = masked_x.mean(axis=0)

    # replace with the most frequent value
    #if replace_by.lower() == "mf":
    #    

    masked_x.set_fill_value(fill_value)

    return masked_x.filled()