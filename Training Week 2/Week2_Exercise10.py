# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 13:48:51 2019

@author: smbatong
"""

def extract_numbers(istring):
    """extract numbers from a string"""
    m=istring.split()
    num_array=[]
    for i in range(len(m)):
        try:
            x=int(m[i])
            num_array.append(x)
        except :
            try:
                x=float(m[i])
                num_array.append(x)
            except: pass  
    return num_array

print(extract_numbers("abd 123 1.2 test 13.2 -1"))     
                