# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 15:05:57 2019

@author: smbatong
"""


def reverse_dictionary(iDictionary):
    Rev={}
    m=[]
    for val in iDictionary.values() :
       for j in range(len(val)):
           m.append(val[j])
    m=list(set(m))
    for i in range(len(m)):
       translation=[]
       for key, val in  iDictionary.items():    
           if m[i] in val:
               translation.append(key)
               Rev[m[i]]=translation
    print( Rev)
    
    
d={'move': ['liikuttaa','run'], 'hide': ['piilottaa', 'salata'], 'six': ['kuusi'], 'fir': ['kuusi']}
reverse_dictionary(d)


    