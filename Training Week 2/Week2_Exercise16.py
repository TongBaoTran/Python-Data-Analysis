# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 15:07:40 2019

@author: smbatong
"""

import numpy as np

def multiplication_table(inum):
    x=np.arange(inum);
    y=x.reshape((inum,1))
    print(x)
    print(y)
    m=x*y;
    return m


print(multiplication_table(4))
