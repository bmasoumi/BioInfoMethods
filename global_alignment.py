#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 19 08:41:23 2018

@author: Beeta
Global Alignment

"""

alphabet = ['A', 'C', 'G', 'T']
score = [[0, 4, 2, 4, 8],
         [4, 0, 4, 2, 8],
         [2, 4, 0, 4, 8],
         [4, 2, 4, 0, 8],
         [8, 8, 8, 8, 8]]

# converts from character to its offset in list alphabet
alphabet.index('A')
# 0
alphabet.index('G')
# 2

# penalty associated with A (from X) mismatching with T (from Y)
score[alphabet.index('A')][alphabet.index('T')]
# 4

# penalty associated with C (from X) being deleted in Y
score[alphabet.index('C')][-1]
# 8

def globalAlignment(x, y):
    # Create distance matrix
    D = []
    for i in range(len(x)+1):
        D.append([0] * (len(y)+1))
        
    # Initialize first column
    for i in range(1, len(x)+1):
        D[i][0] = D[i-1][0] + score[alphabet.index(x[i-1])][-1]

    # Initialize first row
    for j in range(1,len(y)+1):
        D[0][j] = D[0][j-1] + score[-1][alphabet.index(y[j-1])]
        
    # Fill rest of the matrix
    for i in range(1, len(x)+1):
        for j in range(1, len(y)+1):
            distHor = D[i][j-1] + score[-1][alphabet.index(y[j-1])]
            distVer = D[i-1][j] + score[alphabet.index(x[i-1])][-1]
            distDiag = D[i-1][j-1] + score[alphabet.index(x[i-1])][alphabet.index(y[j-1])]
            D[i][j] = min(distHor, distVer, distDiag)
    
    return D[-1][-1]  # return value in bottom right corner



x = 'TATGTCATGC'
y = 'TATGGCAGC'
print(globalAlignment(x,y))
# 12



