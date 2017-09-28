import os
import csv
import filecmp

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

#Sort based on key/column
def mySort(data,col):
#Input: list of dictionaries
#Output: Return a string of the form firstName lastName
	sortbykeys = sorted(data, key = lambda x: x[col])

	return (sortbykeys[0]['First'] + ' ' + sortbykeys[0]['Last'])	



def classSizes(data):
# Input: list of dictionaries
# Output: Return a list of tuples ordered by
# ClassName and Class size, e.g 
# [('Senior', 26), ('Junior', 25), ('Freshman', 21), ('Sophomore', 18)]
	classdict = {}

	for dictionary in data:
		if dictionary['Class'] not in classdict:
			classdict[dictionary['Class']] = 1
		else:
			classdict[dictionary['Class']] += 1

	lizist = []
	for x in classdict.items():
		lizist.append(x)

	return (sorted(lizist, key = lambda x: x[1], reverse = True))




	# Find the most common day of the year to be born
def findDay(a):
	dictcount = {}
	listofdates = []
	listofdates1 = []
	for dictionary in a:
		x = dictionary['DOB'] 
		listofdates.append(x)

	for x in listofdates:
		listofdates1.append((x.split('/'))[1])

	for x in listofdates1:
		if x not in dictcount:
			dictcount[x] = 1
		else:
			dictcount[x] += 1

	return (int((sorted(dictcount, key = lambda x: dictcount[x], reverse = True))[0]))

def findAge(a):
	countofage = 0
	countofpeople = 0
	year = 2017

	for dictionary in a:
		yearborn = (dictionary['DOB'].split('/'))[2]
		age = year - int(yearborn)
		countofage += age
		countofpeople += 1

	return (int(countofage / countofpeople))



def mySortPrint(a,col,fileName):

	sortbycol = sorted(a, key = lambda x: x[col])

	newfile = open(fileName, 'w')

	for item in sortbycol:
		lzt = [][:2] 
		for x in item.values():
			lzt.append(x)
		newfile.write('{},{},{}\n'.format(lzt[0], lzt[1], lzt[2]))


################################################################
## DO NOT MODIFY ANY CODE BELOW THIS
################################################################

## We have provided simple test() function used in main() to print what each function returns vs. what it's supposed to return.
def test(got, expected, pts):
  score = 0;
  if got == expected:
    score = pts
    print(" OK ",end=" ")
  else:
    print (" XX ", end=" ")
  print("Got: ",got, "Expected: ",expected)
  return score


# Provided main() calls the above functions with interesting inputs, using test() to check if each result is correct or not.
def main():
	total = 0
	print("Read in Test data and store as a list of dictionaries")
	data = getData('P1DataA.csv')
	data2 = getData('P1DataB.csv')
	total += test(type(data),type([]),40)
	print()
	print("First student sorted by First name:")
	total += test(mySort(data,'First'),'Abbot Le',15)
	total += test(mySort(data2,'First'),'Adam Rocha',15)

	print("First student sorted by Last name:")
	total += test(mySort(data,'Last'),'Elijah Adams',15)
	total += test(mySort(data2,'Last'),'Elijah Adams',15)

	print("First student sorted by Email:")
	total += test(mySort(data,'Email'),'Hope Craft',15)
	total += test(mySort(data2,'Email'),'Orli Humphrey',15)

	print("\nEach grade ordered by size:")
	total += test(classSizes(data),[('Junior', 28), ('Senior', 27), ('Freshman', 23), ('Sophomore', 22)],10)
	total += test(classSizes(data2),[('Senior', 26), ('Junior', 25), ('Freshman', 21), ('Sophomore', 18)],10)

	print("\nThe most common day of the year to be born is:")
	total += test(findDay(data),13,10)
	total += test(findDay(data2),26,10)
	
	print("\nThe average age is:")
	total += test(findAge(data),39,10)
	total += test(findAge(data2),41,10)

	print("\nSuccessful sort and print to file:")
	mySortPrint(data,'Last','results.csv')
	if os.path.exists('results.csv'):
		total += test(filecmp.cmp('outfile.csv', 'results.csv'),True,10)


	print("Your final score is: ",total)
# Standard boilerplate to call the main() function that tests all your code.
if __name__ == '__main__':
    main()

