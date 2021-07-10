# -*- coding: utf-8 -*-
"""
Created on Fri Feb 19 13:22:57 2021

@author: Keyur
quicksort

Time taken by QuickSort in general can be written as following. 

 T(n) = T(k) + T(n-k-1) + \theta(n)
 
 Worst Case:
T(n) = T(0) + T(n-1) + \theta(n)
which is equivalent to  
T(n) = T(n-1) + \theta(n)

Best Case: 
T(n) = 2T(n/2) + \theta(n)

Average Case: 
T(n) = T(n/9) + T(9n/10) + \theta(n)

Solution of above recurrence is also O(nLogn)
Although the worst case time complexity of QuickSort is O(n^2) 
"""
def partitions(arr,low,high):
    pivot=arr[high]
    pIndex=low
    for j in range(low , high):
        if(arr[j]<pivot):
            arr[j],arr[pIndex]=arr[pIndex],arr[j]
            pIndex=pIndex+1
            
    arr[high],arr[pIndex]=arr[pIndex],arr[high]
    return pIndex


def quicksort(arr,low,high):
    if(low<high):
        pIndex=partitions(arr,low,high)
        quicksort(arr, low, pIndex-1) #Left part divition
        quicksort(arr, pIndex+1 ,high) #Right part divition


A=[5,3,1,7,8,4,9]
n=len(A)
quicksort(A,0,n-1)
print(A)