# -*- coding: utf-8 -*-
"""
Created on Tue Apr 13 12:53:53 2021

@author: Keyur Asodariya
"""
import collections
def bfs(graph,root):
    visited = set()
    queue=collections.deque([root])
    visited.add(root)
    while queue:
        vertex=queue.popleft()
        print(vertex)
        for neighbour in graph[vertex]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)
    
    



graph={0:[1,2],1:[0,3,4],2:[0,5],3:[1,4],4:[1,3],5:[2]}
bfs(graph,2)