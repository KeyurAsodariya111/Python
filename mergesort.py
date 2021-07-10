# -*- coding: utf-8 -*-
"""
Created on Fri Feb 19 11:05:16 2021

@author: Keyur

Mergesort

Time complexity of Merge Sort is  θ(nLogn)
Auxiliary Space: O(n)
Algorithmic Paradigm: Divide and Conquer
"""

def mergesort(A):
   if(len(A)>1):
       mid=int(len(A)/2)
       lefthalf=A[:mid]
       righthalf=A[mid:]
       
       
       mergesort(lefthalf)  #divide till only one element exists
       mergesort(righthalf)  #divide till only one element exists

       i=j=k=0
        
       while (i<len(lefthalf) and j<len(righthalf)):
           if(lefthalf[i]<righthalf[j]):
                A[k]=lefthalf[i]
                i=i+1

           else:
                A[k]=righthalf[j]
                j=j+1
           k=k+1
        
       while(i<len(lefthalf)):
        	A[k]=lefthalf[i]
        	i=i+1
        	k=k+1
        
       while(j<len(righthalf)):
        	A[k]=righthalf[j]
        	j=j+1
	        k=k+1

A=[5,3,1,7,8,4,9]
mergesort(A)
print(A)