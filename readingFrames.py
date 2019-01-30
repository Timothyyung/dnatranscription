#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
import sys

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
    
    
    seq = rseq(seq)

    for i in range(0, len(seq)-2):
        aacid = seq[i:i+3]
        framenum = i%3 + 3
        frames[framenum] = frames[framenum] + adict[aacid] + " "
     
    return frames

def printframes(frames):
    j = 1
    for i in range(0,len(frames)):
        if i <= 2: 
            print "\n\n5'3' Frame " + str(i)
            i += 1
        else:
            print "\n\n3'5' Frame " + str(j)
            j += 1
        
        print frames[i]
        print '\n\nLongest open frame: '
        print findopenframes(frames[i])
        print '__________________  '

def findopenframes(frame):
    openframe = ''
    tframe =''
    framestart = False
    protiens = frame.split(' ')
    for char in protiens:
        if ( char == 'Met' ):
            framestart = True
        elif ( char == 'Stop'):
            framestart = False
            if( len(tframe) > len(openframe)):
                openframe = tframe + 'Stop'
            tframe = ''

        if(framestart == True):
            tframe = tframe + char + ' ' 

    return openframe

if __name__ == "__main__":
    
    aminoacids = aminodict()

    seq = readsequence(sys.argv[1])
    frames = translation(seq,aminoacids)
    printframes(translation(seq,aminoacids))
     
