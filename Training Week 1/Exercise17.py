# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 14:52:33 2019

@author: smbatong
"""

def positive_list(iList):
    def is_positive(x):
        return x>0
    L=list(filter(is_positive,iList))
    return L
    
print(positive_list([2,-2,0,1,-7]))