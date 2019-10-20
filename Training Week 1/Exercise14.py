# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 10:48:06 2019

@author: smbatong
"""

def find_matching(stringList, searchString):
    IndexList=[]
    for i in range(len(stringList)):
        if searchString in stringList[i]:
            IndexList.append(i)
    return IndexList        

print(find_matching(["sensitive", "engine", "rubbish", "comment","men"], "en"))
