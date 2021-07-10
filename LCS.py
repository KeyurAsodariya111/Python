# -*- coding: utf-8 -*-
"""
Created on Fri Mar 26 15:19:41 2021
Longest Common Subseqence 
@author: Keyur Asodariya
"""
def lcs(X,Y):
    m=len(X)
    n=len(Y)
    L=[[0 for i in range(n+1)]for j in range(m+1)]
    
    for i in range(1,m+1):    #i for X
        for j in range(1,n+1): #j for Y
            if(X[i+1]==Y[j-1]):
                L[i][j]=1+L[i-1][j-1]
            else:
                L[i][j]=max(L[i-1][j],L[i][j-1])
    return L[m][n]    

    
X="LONGEST"
Y="STONE"
print("Longest Common Subseqence Lenght is:",lcs(X,Y))