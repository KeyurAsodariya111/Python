# -*- coding: utf-8 -*-
"""
Created on Fri Apr 23 15:35:41 2021

@author: Keyur Asodariya
"""
def createadjmatrix(V,G):
    adjmatrix=[[0 for i in range(V)]for j in range(V)]
    for i in range(len(G)):
        adjmatrix[G[i][0]][G[i][1]]=G[i][2]
        adjmatrix[G[i][1]][G[i][0]]=G[i][2]
    return adjmatrix

def prims(V,G):
    adjmatrix=createadjmatrix(V,G)
    print(adjmatrix)


a,b,c,d,e,f=0,1,2,3,4,5
graph=[[a,b,2],[a,c,3],[b,d,3],[b,c,5],[b,e,4],[c,e,4],[d,e,2],[d,f,3],[e,f,5]]

prims(6,graph)