#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re


""" This function creates the dictionary that has references to what sequence of neucleotides become what amino acids 
We store the references in a text file and use it to create the dictionary"""

def aminodict():
    adict = {}
    with open('./aminoacids.txt') as infile:
        
        line = infile.readline()
        while line:
            lines = line.split()
            adict[lines[0]] = lines[1]
            line = infile.readline()
    return adict

""" Reverses a given sequence (both order and matching pair) """

def rseq(seq):
    acids = {
            'A' : 'T',
            'T' : 'A',
            'G' : 'C',
            'C' : 'G'
            }
    s = ""
    for char in seq:
        s = acids[char] + s
    return s
    
    
""" reads a sequence file and removes all unnessearry text from the sequence e.g. anything not agct or AGCT """

def readsequence(filename):
    with open(filename, 'r') as infile:
        seq = infile.read()
    return re.sub('[^acgtACGT]',"",seq).upper()

""" translates a sequence into a string of amino acids """

def translation(seq, adict):
    frames = ["" for i in range (0,6)]

    
    for i in range(0,len(seq)-2):
        aacid = seq[i:i+3]
        framenum = i%3
        frames[framenum] = frames[framenum] + adict[aacid] + " "

        aacid = rseq(aacid)
        frames[(framenum) + 3] = adict[aacid] + " " + frames[(framenum) +3]

    
    return frames

def printframes(frames):
    order = [0,1,2,5,4,3]
    i = j = 1
    for num in order:
        if num <= 2: 
            print "\n\n5'3' Frame " + str(i)
            i += 1
        else:
            print "\n\n3'5' Frame " + str(j)
            j += 1

        print  frames[num]


if __name__ == "__main__":

    aminoacids = aminodict()

    seq = readsequence('./seq.txt')

    printframes(translation(seq,aminoacids))

