# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 13:07:12 2019

@author: smbatong
"""

class Rational:
    def __init__(self, numerator, denominator):
        self.rational=numerator/denominator
    
    def showme(self):
        print(f'{self.rational} is the rational number')
        
    def __add__(self, other):
        return self.rational+other.rational
    
    def __subtract__(self, other):
        return self.rational-other.rational 
    
    def __multiply__(self, other):
        return self.rational*other.rational
    
    def __division__(self, other):
        return self.rational/other.rational
    
    def __isgreater__(self, other):
        return self.rational>other.rational
    
    def __issmaller__(self, other):
        return self.rational<other.rational
    
    def __isequal__(self, other):
        return self.rational==other.rational
    

x=Rational(1,4)
y=Rational(2,8)
x.showme()
y.showme()
m=x.__add__(y)
print(m)
m=x.__issmaller__(y)
print(m)





        