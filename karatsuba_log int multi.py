# -*- coding: utf-8 -*-
"""
Created on Mon May  3 10:09:13 2021

@author: Keyur Asodariya

Time com:- O(n^1.585)
"""
X=int(input("Enter number 1 :"))
Y=int(input("Enter number 2 :"))
def karatsuba(X,Y):
    #base condition
    if X<10 or Y<10:
        return X*Y
    
    m=max(len(str(X)),len(str(Y)))
    if m%2!=0:
        m-=1
    a,b=divmod(X, 10**int(m/2))
    c,d=divmod(Y, 10**int(m/2))
    
    ac=karatsuba(a,c)
    bd=karatsuba(b,d)
    ad_bc=karatsuba((a+b),(c+d))-ac-bd
    
    return (ac*(10**m))+(ad_bc*(10**int(m/2)))+bd


print(karatsuba(X,Y))