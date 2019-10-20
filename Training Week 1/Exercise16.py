# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 11:01:21 2019

@author: smbatong
"""

def transform(string1,string2):
    ResultList=[]
    string1a=list(map(int,string1.split()))
    string2a=list(map(int,string2.split())) 
    for x1, x2 in zip(string1a,string2a):
        ResultList.append(x1*x2)
    return ResultList

print(transform("1 5 3", "2 6 -1"))