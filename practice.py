import os
import csv

def getData(filename):
#Input: file name
#Ouput: return a list of dictionary objects where 
#the keys will come from the first row in the data.

#Note: The column headings will not change from the 
#test cases below, but the the data itself will 
#change (contents and size) in the different test 
#cases.
	file1 = open(filename)
	data = csv.reader(file1)
	sorteddata = [(First, Last, Email, Class, DOB) for (First, Last, Email, Class, DOB) in list(data)]
	
	LOD = []
	headers = sorteddata[0]
	
	for tup in sorteddata[1:]:
		newdict = {}
		for x in (list(range(len(tup)))):
			newdict[headers[x]] = tup[x]
		LOD.append(newdict)

	return (LOD)


mekk = (getData('P1DataA.csv'))

def mySort(data,col):
#Input: list of dictionaries
#Output: Return a string of the form firstName lastName
	sortbykeys = sorted(data, key = lambda x: x[col])
	for item in sortbykeys:
		lzt = []
		for x in item.values():
			lzt.append(x)
		print (lzt)

print (mySort(mekk, 'First'))







