# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 15:03:04 2019

@author: smbatong
"""


def acronyms(istring):
    Acr=[]
    istring.strip('"()')
    bad_chars = ['(', ')', '.', ","] 
    for i in bad_chars : 
        istring = istring.replace(i, '') 
    L=istring.split()
    for i in range(len(L)):
        if (len(L[i])>=2 and L[i].isupper()):
            Acr.append(L[i])
            
    return Acr
    



print(acronyms("""For the purposes of the EU General Data Protection Regulation (GDPR), the controller of your personal information is International Business Machines Corporation (IBM Corp.), 1 New Orchard Road, Armonk, New York, United States, unless indicated otherwise. Where IBM Corp. or a subsidiary it controls (not established in the European Economic Area (EEA)) is required to appoint a legal representative in the EEA, the representative for all such cases is IBM United Kingdom Limited, PO Box 41, North Harbour, Portsmouth, Hampshire, United Kingdom PO6 3AU."""))