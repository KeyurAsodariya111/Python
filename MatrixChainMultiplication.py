# -*- coding: utf-8 -*-
"""
Created on Fri Apr  2 15:26:49 2021
Matrix chain multiplication

Time Complexity:= O(n^3)
Auxiliary space := O(n^2)
@author: Keyur Asodariya
"""

def MatrixChainMultiplication(d,n):
    m=[[0 for i in range(n)]for j in range(n)]
    for i in range(1,n):
        m[i][i]=0   #principle diagonal
    for D in range(1,n-1): #difference matrix
        for i in range(1,n-D):
            for j in range(1,n-D):
                j=i+D
                m[i][j]=10000
                for k in range(i,j):
                    q=m[i][k]+m[k+1][j]+d[i-1]*d[k]*d[j]
                    if (q < m[i][j]):
                        m[i][j] = q
    return m[1][n-1]


d=[5,4,6,2,7]
size=len(d)
m=MatrixChainMultiplication(d,size)
print(m)