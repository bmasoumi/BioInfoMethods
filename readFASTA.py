#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 10 09:51:31 2018

@author: Beeta
Download and parse a genome

"""



#!wget --no-check url

# read a genome from a FASTA file
def readFASTA(filename):
    genome = ''
    with open(filename, 'r') as f:
        for line in f:
            if not line[0] == '>':
                genome += line.rstrip()
    return genome
    
    
genome = readFASTA('lambda_virus.fa')
print(genome[:100], len(genome)) #len should be 48502


# count frequency of each base
# using dictionary 
counts = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
for base in genome:
    counts[base] +=1
print(counts)
    
# count frequency of each base using python modules
import collections
collections.Counter(genome)

