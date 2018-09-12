#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 11 10:31:09 2018

@author: Beeta
Implementation of exact matching algorithms
- Naive Exact Matching(Brute Force)

"""

def readFASTA(filename):
    genome = ''
    with open(filename, 'r') as f:
        for line in f:
            if not line[0] == '>':
                genome += line.rstrip()
    return genome
                

genome = readFASTA('phix.fa')   
    
#=============================
# Naive exact matching
# aka Brute Force
#=============================
# returns offsets of pattern p in text t
def BruteForce(p, t):
    occurrences = []
    for i in range(len(t)-len(p)+1): # loop over alignment
        match = True
        for j in range(len(p)): # loop over characters
            if t[i+j] != p[j]:  # compare characters
                match = False   # mismatch
                break
        if match:   # allchars matched
            occurrences.append(i)
    return occurrences

p = 'word'
t = 'this sentence contains a word'
occurrences = BruteForce(p, t)
print(occurrences) # 25 is the answer
min_no_comparisons = len(t)-len(p)+1
max_no_comparisons = len(p)*(len(t)-len(p)+1)
print(min_no_comparisons, max_no_comparisons) #answer is 26 & 104

p = 'AG'
t = 'AGCCCTTTGATAGTTTCAG'
BruteForce(p,t) # answer is [0, 11, 17]
# test the answer
print(t[:2], t[11:13], t[17:19])

# generate artifical reads from random positions in a given genome phix
import random

def generateReads(genome, numReads, readLen):
    reads = []
    for _ in range(numReads):
        start = random.randint(0, len(genome)-readLen) - 1
        reads.append(genome[start: start+readLen])
    return reads


reads = generateReads(genome, 100, 100)  
print(reads) 
                
# matching artifical reads
# how many of these reads match the genome exactly
# obviously the answer should be all of them bc 
# these are generated from this genome and there is no error involved

numMatched = 0
for r in reads:
     matched = BruteForce(r ,genome)
     if len(matched) > 0:
         numMatched += 1
print('%d / %d reads matched the genome exactly' % (numMatched, len(reads)))


"""
# using python string methods
example = 'this sentence contains a word'
example.find('word') #find method returns the offset of the pattern (the leftmost)
# 'word' occurs at offset 25
"""

# matching real reads 
# from a FASTQ file ERR266411_1.for_asm.fastq
# that has real reads from phix

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


phix_reads, _ = readFASTQ('ERR266411_1.for_asm.fastq')
print(phix_reads, len(phix_reads))
            
            
numMatched = 0
total = 0
for r in phix_reads:
    matched = BruteForce(r, genome) 
    total += 1
    if len(matched) > 0:
        numMatched += 1
print('%d / %d reads matched the genome' % (numMatched, total))
# answer is 502 / 10000 reads matched the genome
# bc of sequencing errors or 
# bc the reference genome is double stranded and we checked only one
# now lets chnage it to matching only 30 first bases of reads 
numMatched = 0
total = 0
for r in phix_reads:
    r = r[:30]
    matched = BruteForce(r, genome) 
    total += 1
    if len(matched) > 0:
        numMatched += 1
print('%d / %d reads matched the genome' % (numMatched, total))
# answer is 3563 / 10000 reads matched the genome
# still very low matching
# so lets do the same thing for the reverse complement of the read

def reverseComplement(s):
    complement = {'A':'T', 'C':'G', 'T':'A', 'G':'C', 'N':'N'}
    t = ''
    for base in s:
        t = complement[base] + t
    return t
reverseComplement(phix_reads[1])


numMatched = 0
total = 0
for r in phix_reads:
    r = r[:30]
    matched = BruteForce(r, genome) # matches in forward strand
    matched.extend(BruteForce(reverseComplement(r), genome)) # matches in reverse strand
    total += 1
    if len(matched) > 0:
        numMatched += 1
print('%d / %d reads matched the genome' % (numMatched, total))
# answer is 8036 / 10000 reads matched the genome
# much better result
        
   













