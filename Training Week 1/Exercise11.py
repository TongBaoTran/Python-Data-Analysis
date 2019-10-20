# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 13:07:22 2019

@author: smbatong
"""

def interleave(ilist1, ilist2,ilist3):
    t=list(zip(ilist1,ilist2,ilist3))
    m=[]
    for i in range(len(t)):
       m.extend(list(t[i]))
    return m
        
print(interleave([1,2,3], [20,30,40], ['a', 'b', 'c']))