#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 10 10:23:20 2018

@author: Beeta
Download and parse a FASTQ file

"""

# store sequences and qualities in lists
def readFASTQ(filename):
    sequences = []
    qualities = []
    with open(filename, 'r') as f:
        while True: 
            f.readline()
            seqs = f.readline().rstrip()
            f.readline()
            quals = f.readline().rstrip()
            if len(seqs) == 0:
                break
            sequences.append(seqs)
            qualities.append(quals)
    return sequences, qualities

seqs, quals = readFASTQ('SRR835775_1.first1000.fastq')
print(seqs[:5])
print(quals[:5])

# convert phred33 to Quality score
def phred33ToQ(quals):
    return ord(quals) - 33

phred33ToQ('#') 
#returns 2 which a low quality value which means 
#low confidence for that base, which means the base might be wrong
phred33ToQ('J') 
#returns 41 which a high quality
#less than 1 in 10,000 chnace that the base might be wrong



# generate a histogram of quality values 
# plot a distribution of quality values
def createHist(qualities):
    hist = [0] * 50 # keep track of frequency of each quality score we've seen
    for quals in qualities: # for each string of quality values in our list qualities
        for phred in quals: # step through each quality score in each string
            q = phred33ToQ(phred)
            hist[q] +=1
    return hist

h = createHist(quals)
print(h, len(h))
 
import matplotlib.pyplot as plt
plt.bar(range(len(h)), h)
#plt.show()


# calculate the G and C frequency
# GC content
def GCcontent(reads):
    #reads are max 100 bases
    gc = [0] * 100
    totals = [0] * 100
    for read in reads:
        for i in range(len(read)):
            if read[i]=='C' or read[i]=='G':
                gc[i] += 1
            totals[i] += 1
    for i in range(len(gc)):
        if totals[i] > 0:
            gc[i] /= float(totals[i])
    return gc

gc = GCcontent(seqs)
print(gc)
import matplotlib.pyplot as plt
plt.plot(range(len(gc)), gc)
plt.show()

# total number of each base 
import collections
count = collections.Counter()
for s in seqs:
    count.update(s)
print(count)
# Counter({'G': 28742, 'C': 28272, 'T': 21836, 'A': 21132, 'N': 18})
# GC content is above 50% in this sequence which is part of human genome


            










  
    
    
    
    
    
    
    
    
    
    


           
