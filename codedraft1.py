#!/usr/bin/python2

#this code should be run first using the Fish taxonomy file. 
#The output will be one file per sample site, which should be used as the input for the R code

#Usage = python2 codedraft1.py Fish_taxonomy_file.txt

import re
import string
import sys
import os

usageerror = ("""
INPUT ERROR. 
/nameofourprogram/ requires 2 inputs.
Usage:
	python codedraft.py inputfile
""")

if len(sys.argv) != 2:
	print usageerror
else:
	inputfile = sys.argv[1]
	openfile = open(inputfile, "r")

#This works out the number of columns in the input file

with open(inputfile, "r") as f:
	h = f.readline()
	header = h.split("\t")
	headlen = len(header)
	colrange = range(1,headlen - 1)
	
masterlist = [0]

for x in colrange:
        masterlist.append(header[x])

openfile.readline() #skips the 1st line
for line in openfile:
#	if 
	line = line.strip()
        Col = line.split("\t")
	if len(Col) == headlen:                
		for x in colrange:
			if Col[x] != "0":
				if ';' not in line:
					sys.stderr.write("Taxonomy data must be seperated by semicolons. Please check input file")
				else:
					sp = line.split(';')[-1]
					masterlist[x] =  masterlist[x] + ';' + sp
for i in colrange:
	filename = "column" + str(i) + ".txt"	
	with open(filename, 'w') as output:
		output.write(masterlist[i])

# Puts each species on seperate lines; removes any repeats

path = os.listdir('.')

for filename in path:
	if 'column' in filename:
		outfile1 = str('sample') + filename
		with open(filename, "r") as inn:
			sep =  inn.read().replace(';','\n')
		os.remove(filename)
		with open(outfile1, "w+") as out:
			out.write(sep)		
		unique = []
		outfile2 = "final" + outfile1
		openoutfile2 = open(outfile2, "w")
		for line in open(outfile1,"r"):
			if line not in unique:
				openoutfile2.write(line)
				unique.append(line)
		os.remove(outfile1)
