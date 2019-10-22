# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 15:15:14 2019

@author: smbatong
"""

import numpy as np

def vector_angles(array1, array2):
    inner_product=np.sum(array1*array2, axis=1)
    x=np.sqrt(np.sum(array1**2, axis=1))
    y=np.sqrt(np.sum(array2**2, axis=1))
    angle_vector=inner_product/(x*y)
    angle_vector = np.clip(angle_vector, a_min = -1, a_max = 1) 
    angle=np.arccos(angle_vector)
    return angle


array1=np.array([[1,2,3], [4,5,6]])
array2=array1
print( vector_angles(array1, array2))




    
           
    