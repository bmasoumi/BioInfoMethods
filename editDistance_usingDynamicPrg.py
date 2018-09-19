#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 18 13:07:43 2018

@author: Beeta

calculating edit distance using dynamic programming


"""
# very slow implementation
def editDistRecursive(x, y):
    if len(x) == 0:
        return len(y)
    elif len(y) == 0:
        return len(x)
    else:
        distHor = editDistRecursive(x[:-1], y) + 1
        distVer = editDistRecursive(x, y[:-1]) + 1
        if x[-1] == y[-1]:
            distDiag = editDistRecursive(x[:-1], y[:-1])
        else:
            distDiag = editDistRecursive(x[:-1], y[:-1]) + 1
        return min(distHor, distVer, distDiag)




def editDistance(x, y):
    D = []
    for i in range(len(x)+1):
        D.append([0]*(len(y)+1))
        
    for i in range(len(x)+1):
        D[i][0] = i
    for i in range(len(y)+1):
        D[0][i] = i
        
    for i in range(1, len(x)+1):
        for j in range(1, len(y)+1):
            distHor = D[i][j-1]+1 #corresponds to skip in y
            distVer = D[i-1][j]+1 
            if x[i-1] == y[j-1]:
                distDiag = D[i-1][j-1]
            else:
                distDiag = D[i-1][j-1] + 1
            D[i][j] = min(distHor, distVer, distDiag)
    return D[-1][-1] #edit distance is the value at the bottom right corner of matrix


%%time
x = 'shake spea'
y = 'Shakespear'
editDistRecursive(x, y)
                
%%time
x = 'shake spea'
y = 'Shakespear'
editDistance(x, y)
                
                
                
                
                
                
                
                
                
            
        