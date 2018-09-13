#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 13 11:16:00 2018

@author: Beeta
implementing a k-mer index

"""
# a bit of understanding here
class beeta(object):
    m = 123
    def __init__(self):
        self.m = 456
        
beetaclone = beeta()
print(beeta.m) #answer is 123
print(beetaclone.m) #answer is 456






# implementing a substring index for a text t 
# which we can use to match a pattern against it

import bisect

# create an index object that has 2 methods
# 1st method: preprocessing/initialization
# querying

class Index(object):
    # preprocessing the text t
    # create index for all substrings of size k, k-mers
    def __init__(self, t, k):
        self.k = k
        self.index = []
        for i in range(len(t) - k + 1): # for each k-mer
            self.index.append((t[i:i+k], i)) # add (k-mer, offset) pair
        self.index.sort() # alphabetically by k-mer
    # query: return index hits for first k-mer of p 
    def query(self, p):
        kmer = p[:self.k] # query with first k-mer
        i = bisect.bisect_left(self.index, (kmer, -1))
        hits = []
        while i < len(self.index): # collect matching index entries
            if self.index[i][0] != kmer:
                break
            hits.append(self.index[i][1])
            i += 1
        return hits
    
def queryIndex(p, t, index):
    k = index.k
    offsets = []
    for i in index.query(p):
        if p[k:] == t[i+k:i+len(p)]: #verify that rest of p matches
            offsets.append(i)
    return offsets

t = 'GCTAGCATCTACAGTCTA'
p = 'TCTA'

t = 'ACTTGGAGATCTTTGAGGCTAGGTATTCGGGATCGAAGCTCATTTCGGGGATCGATTACGATATGGTGGGTATTCGGGA'
p = 'GGTATTCGGGA'

index = Index(t, 2) # k has to be less than p
print(queryIndex(p, t, index))
# [7, 14]




    

        
