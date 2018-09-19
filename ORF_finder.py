#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 19 09:32:46 2018

@author: Beeta

ORF Finder

"""

def readFasta(filename):
    
    seqs = {}
    num_records = 0
    new_d = {}
    with open(filename) as f:
        for line in f:
            line = line.rstrip()
            if line[0] == '>':
                num_records +=1
                words = line.split()
                name = words[0][1:]
                seqs[name] = ''
            else:
                seqs[name] = seqs[name]+line
      
        #for name in seqs:
           # print(name, seqs[name])
        
        #print("type is", type(seqs[name]))
        for name in seqs:    
            #print(name, len(seqs[name]))
            new_d[name] = len(seqs[name]) 
            print(name, new_d[name])
        
       
        
        key_max = max(new_d.keys(), key=(lambda k: new_d[k])) 
        print('identifier: ', key_max, 'Maximum Value: ', new_d[key_max])
        #print(name for names in new_d if new_d[name] == key_max)
        for name in new_d:
            if new_d[name] == key_max:
                print('another maximum at:', new_d[name] )
            else:
                break        
        print('no more maximum')
        
        
        key_min = min(new_d.keys(), key=(lambda k: new_d[k]))
        print('identifier: ', key_min, 'Minimum Value: ', new_d[key_min])
        for name in new_d:
            if new_d[name] == key_min:
                print('another minimum at:', new_d[name])
            else:
                break
        print('no more minimum')
        f.close()

        
            

def stop_codon_count(dna):
   
    stop_codons = ['tag', 'tga', 'taa']

    for frame in range(0,3):
        stop_count = 0
        #print('now frame', frame)
        for i in range(frame, len(dna), 3):
            if dna[i:i+3].lower() in stop_codons:
                stop_count += 1
                i += 3
        print('frame:', frame, 'stop count:', stop_count)
        #return frame, stop_count
        

def start_codon_count(dna):
    
    start_codons = ['atg']
        
    for frame in range(3):
        start_count = 0
        for i in range(frame, len(dna), 3):
            if dna[i:i+3].lower() in start_codons:
                start_count +=1
                i +=3
        print('frame:', frame, 'start count:', start_count)
        
import sys
        
        
def orf_finder(filename):
    seqs = {}
    start_codons = ['atg']
    start_loc = []
    stop_codons = ['tag', 'tga', 'taa']
    stop_loc = []
    
    with open(filename) as f:
        for line in f:
            line = line.rstrip()
            if line[0] == '>':
                words = line.split()
                name = words[0][1:]
                seqs[name] = ''
            else:
                seqs[name] = seqs[name] + line

    
    for name in seqs:
        print(name)
        stop_codon_count(seqs[name])
        start_codon_count(seqs[name])
        
        for frame in range(3):
            for i in range(frame, len(seqs[name]), 3):
                if seqs[name][i:i+3].lower() in start_codons:
                    start_loc = str(i+1).splitlines()
                    print('start_loc is', start_loc)
                if seqs[name][i:i+3].lower() in stop_codons:
                    stop_loc = str(i+1).splitlines()
                    print('stop_loc is', stop_loc)
        
        
        #frame, stop_count = stop_codon_count(seqs[name])
        #print('orf frame:', frame, 'orf stop_count:', stop_count)
        
        
orf_finder('dna.example.fasta')


        
        
