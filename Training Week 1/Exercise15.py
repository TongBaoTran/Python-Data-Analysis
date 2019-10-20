# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 10:53:15 2019

@author: smbatong
"""

L=[(i,j) for i in range(1,6)
         for j in range(1,6)
         if i+j==5]

for i in range(len(L)):
  print(L[i])