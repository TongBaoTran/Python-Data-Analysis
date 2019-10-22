# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 14:07:37 2019

@author: smbatong
"""

import numpy as np

def get_rows(iarray):
    m=np.shape(iarray)
    rowno=m[0]
    row_list=[]
    for i in range(rowno):
        row_list.append(iarray[i,:])
    return row_list    




def get_columns(iarray):
    m=np.shape(iarray)
    colno=m[1]
    col_list=[]
    for i in range(colno):
        col_list.append(iarray[:,i])
    return col_list
        
a = np.array([[5, 0, 3, 3],
              [7, 9, 3, 5],
              [2, 4, 7, 6],
              [8, 8, 1, 6]])
print(get_rows(a))
print(get_columns(a))


    
    
#def get_colums(iarray):