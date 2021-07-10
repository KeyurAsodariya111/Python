# -*- coding: utf-8 -*-
"""
Created on Tue Feb 23 13:07:57 2021
Time Complexity: O(n+k)
Auxiliary Space: O(n+k)
@author: Keyur
"""

def countsort(arr):
    freq=[0 for i in range(256)]
    for j in arr:
        freq[ord(j)]+=1  #incrementin the count for the character
    
    sorted_string=""
    for i in range(256):
        for j in range(freq[i]):
            sorted_string+=chr(i)
    return sorted_string




arr="problesolving"
sorted_string=countsort(arr)
print(sorted_string)