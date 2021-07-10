# -*- coding: utf-8 -*-
"""
Created on Wed Apr 14 14:40:01 2021

@author: Keyur Asodariya
"""
import collections
def dfs(graph,root):
    visited = set()
    stack=[root]
    while stack:
        vertex=stack.pop()
        if vertex not in visited:
            print(vertex)
            visited.add(vertex)
            visited.add(vertex)
            stack.extend(graph[vertex])


graph={1:[2,3],2:[1,4,5],3:[1,5],4:[2,6],5:[2,3,6],6:[4,5,7],7:[6]}
dfs(graph,1)
