# -*- coding: utf-8 -*-
"""
Created on Fri Feb 26 10:32:06 2021

fractionalknapsack

Time complexity = nlogn
space = O(N)

@author: Keyur
"""

def fractionalknapsack(cost,weight,capacity):
    index=list(range(len(cost)))#declare the indices of the products
    ratio=[c/w for c,w in zip(cost,weight)]
    index.sort(key = lambda i : ratio[i],reverse=True)#sorts in desc order
    profit=0
    quantity=[0]*len(cost)
    product=[]
    
    for i in index:
        if(weight[i]<=capacity):#Less or equal to the capacity
            profit+=cost[i]
            capacity-=weight[i]
            quantity[i]=weight[i]
            product=product+[i]
            
        else:                   #greater than capacity
            #profit+=cost[i]*(capacity/weight[i])
            profit+=(cost[i]/weight[i])*capacity
            quantity[i]=capacity
            product=product+[i]
            break
    return profit,quantity,product
    
    
  
cost=[100,60,120]
weight=[20,10,30]
capacity=50
profit,quantity,product=fractionalknapsack(cost,weight,capacity)
print(profit)
print(quantity)
print(product)

#Lambda fuction in python --> macros in c language
#addition=lambda num1,num2 : num1 + num2
#print(addition(60, 5))
