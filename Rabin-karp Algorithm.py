# -*- coding: utf-8 -*-
"""
Created on Mon Apr 26 10:08:17 2021
Rabin-karp Algorithm
o(m+n)--->O(n) n is large
@author: Keyur Asodariya
"""

text="python"
pattern="th"

X=len(text)
Y=len(pattern)
d=256 #positional base
flag=0
sumP=0
for i in  range(Y):
    sumP=sumP+ (ord(pattern[i])*(d**(Y-1-i)))  #sum of pattern
    
sumT=0
for i in  range(Y):
    sumT=sumT+ (ord(text[i])*(d**(Y-1-i)))  #sum of text
    
if(sumT==sumP):
    print("pattern is substring of the given text,fount at ",i-Y+1)
    flag=1
    
    
for i in range(Y,X):
    sumT=(sumT-(ord(text[i-Y])*(d**(Y-1))))*d+ord(text[i])
    
    if(sumT==sumP):
        print("Pattern is substring of the given text,fount at ",i-Y+1)
        flag=1
        
        
if(flag==0):
    print("Pattern is not substring of the given text")
    