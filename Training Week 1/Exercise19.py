# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 15:59:47 2019

@author: smbatong
"""

def sum_equation(iList):
    h=""
    if iList==[]:
        h="O = O"
    else:
        for i in range(len(iList)):
            h=h+str(iList[i])+' + '
    h=h.rstrip('+ ')+' = '+str(sum(iList))
    return h

print(sum_equation([1,5,7]))