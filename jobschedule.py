# -*- coding: utf-8 -*-
"""
Created on Mon Mar  1 18:29:01 2021
Job Sequencing
Time complexity  = n^2
@author: Keyur
"""
def jobschedule(arr,t):
    for i in range(len(arr)):
        for j in range(len(arr)-1-i):
            if(arr[j][2] < arr[j+1][2]):
                arr[j],arr[j+1]=arr[j+1],arr[j]
                
                
    result=[False]*t
    job=['0']*t
    
    for i in range(len(arr)):
        for j in range((arr[i][1]-1),-1,-1):
            if(result[j] is False):
                result[j]=True
                job[j]=arr[j][0]
                break
            
    print(job)
                

arr=[['a',2,100],['b',1,10],['c',2,30],['d',2,250],['e',3,15]]
jobschedule(arr,3)
