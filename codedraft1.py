#!/usr/bin/python2

#This script takes an eDNA output file (with columns of different locations and taxonomy information in the last one), and will extract the species name (if applicable)

#Usage = python2 codedraft.py inputfile

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

path = os.listdir('.')

# now need to work out how to rename the output file as the sample name

#for filename in path:
#	if 'finalsamplecolumn' in filename:
#		openfile = open(filename, "r")
#		with openfile as f:
#			for line in f:
#			print f.readline()
#			print firstline

#		print openfile

	#	with open(outfile2,"r") as g:
	#		g.readline()
		#		print line
#			print g.readline()
#			top = g.readline()
#			print top
#			top = lines.strip()
			#newname = str("/") +  top + str("/.txt")
#			print lines
#		os.rename(outfile2, newname)
		
#		open(filename, 'w').close()
	#	outfile = open(outfilename, "w")
#		for line in open

#		for line in inn:
#					out.write(line.replace(';','\n'))



	#	for line in f
	         #      f.read().replace(';', '\n')
#		with open(outfilename, "w+") as x:
#			x.write(sep)
#                       	outfile = open(outfilename, "w")
#			for line in filename:
   #                            	if line not in unique:
 #                                      	outfile.write(line)
  #                                     	unique.append(line)
#		        outfile = open(outfilename,"w+")
#			unique = []
#			for line in filename:
#				if line not in unique:
#					outfile.write(line)
#					unique.append(line)
#                       with open(outfilename) as openfile: 	
			
#for line in x:
#					if line not in unique:
 #               	               		x.write(line)
  #                     	        		unique.append(line)	
#		os.remove(filename)

#for filename in cwd:
#	if 'column' in filename:
#		with open(filename) as g:
		


#			firstline  = g.readline()
#			newname = firstline.strip() + ".txt"
#			unique = []
#			for line in outfile:
#				if line not in unique:
#					outfile.write(line)
#					unique.append(line)
#		os.rename(outfilename, newname)



			#	if line not in newlines:
#					newlines.append(line)
	#	unique1 = []
		#	outfile = open(sample
	#	for line in open(filename, 'r'):
	#		if line not in unique1: #if the species is not a duplicate
	 #              		filename.write(line)


#input_file = "input.txt"
#with open(input_file, "rb") as fp:
 #   lines = fp.readlines()
  #  new_lines = []
   # for line in lines:
    #    #- Strip white spaces
     #   line = line.strip()
   #     if line not in new_lines:
  #          new_lines.append(line)

 #	                	unique1.add(line)



#unique2 = set() # holds unique species in sample 2
#outfile2 = open("sample2.txt", "w")
#for line in open("s2temp.txt", "r"):
 #	 if line not in unique2: #if the species is not a duplicate
  #              outfile2.write(line)
   #             unique2.add(line)
#os.remove("s2temp.txt")




#outfile1.close()
#os.remove("s1temp.txt")
#lines_seen = set() # holds lines already seen
#outfile = open(outfilename, "w")
#for line in open(infilename, "r"):
 #   if line not in lines_seen: # not a duplicate
  #      outfile.write(line)
   #     lines_seen.add(line)
#outfile.close()


#		unique = set() # holds unique species in sample 1
#outfile1 = open("sample1.txt", "w")
#		for line in open("s1temp.txt", "r"):
#	if line not in unique1: #if the species is not a duplicate
#               outfile1.write(line)
 #                      unique1.add(line)
#outfile1.close()
#os.remove("s1temp.txt")











#for f in sample_*.txt:
#	f.append("hello)

#	print masterlist[i]                       
#print masterlist[1]

#makes a masterlist with as many entries as there are columns
#list with all seperated by tab
#now you need to take each entry in the list, make it its own document called the 1st entry

# if Col[2] != "0" and len(Col) >3:
#                Element_list = line.split(';')[-1]
#                sample2.append(Element_list)
#                output2.write(Element_list)


#put every sample as a key in the dictionary. key will come from the header - the sample names
#when you read each line, everytime you are in a particular elementt, tell python to relatte the position with a particular key
#store a variable called header
#header = [filler, s1, s2, s3]
#like header[1] will give u s1
#for x in range:
#	header[x] will giev u samples 1
#havea dctionary called A with all the samples in it
#do some math *have a counter)

#for line in openfile:
#	if line < 1:
 #       	line = line.strip()
  #      	Col = line.split("\t")
#		for x in colrange:
#			masterlist.append(Col[x])

#RecorNum = 0
#for line in openfile:
 #       line = line.strip()
#	Col = line.split("\t")
#	print len(Col)
#	masterlist.append(header[1])

#	if len(Col) == headlen: #only work w/ lines withthe same dimension of the header 
#		for x in colrange:
			
#	print Col[1]
		#	if Col[x] != "0" and len(Col[x]) >3: #if the item in the 2nd column does not equal 0 and the number of columns is > 3
#                Elementlist = line.split(';')[-1] #split the line at the last ;
#                sample1.append(Elementlist)
#                output1.write(Elementlist)
#        if Col[2] != "0" and len(Col) >3:
#                Element_list = line.split(';')[-1]
#                sample2.append(Element_list)
#                output2.write(Element_list)
#output1.close()
#output2.close()

#unique1 = set() # holds unique species in sample 1
#outfile1 = open("sample1.txt", "w")
#for line in open("s1temp.txt", "r"):
#	if line not in unique1: #if the species is not a duplicate
#		outfile1.write(line)
 #      		unique1.add(line)
#outfile1.close()
#os.remove("s1temp.txt")
#unique2 = set() # holds unique species in sample 2
#outfile2 = open("sample2.txt", "w")
#for line in open("s2temp.txt", "r"):
 #       if line not in unique2: #if the species is not a duplicate
  #              outfile2.write(line)
   #             unique2.add(line)
#os.remove("s2temp.txt")
