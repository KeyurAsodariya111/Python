# -*- coding: utf-8 -*-
"""
Created on Fri Mar 12 15:18:08 2021
#Time Complecity T(n)=2T(n/2)+1 ==> O(n)
@author: Keyur Asodariya
"""
def power(x,n):
    if(n==0):           #base
        return 1
    elif(int(n%2)==0):  #even
        return (power(x,int(n/2))*power(x,int(n/2)))
    else:
         return (x*power(x,int(n/2))*power(x,int(n/2)))
        

x=2
n=5  #2^5

print(power(x,n))