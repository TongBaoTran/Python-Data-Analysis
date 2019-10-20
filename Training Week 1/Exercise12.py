# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 13:40:31 2019

@author: smbatong
"""

def distinct_characters(istringList):
    Result_Dictionary={}
    for i in range(len(istringList)):
        Result_Dictionary[istringList[i]]=len(set(istringList[i]))
    return Result_Dictionary

print(distinct_characters(["check", "look", "try", "pop"]))
    