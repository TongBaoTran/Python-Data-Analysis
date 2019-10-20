# -*- coding: utf-8 -*-
"""
This module includes functions to calculate the hypothenuse and area of a right triangle
"""
__version__='2019'
__author__='Tran Tong'

from math import *

def hypothenuse(x,y):
    """Calculating the hypothenuse"""
    h=sqrt(x**2+y**2)
    return h
    
def area(x,y):
    """Calculating the area of the right triangle"""
    area=1/2*x*y
    return area

