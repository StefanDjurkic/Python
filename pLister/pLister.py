# pLister.py
# Stefan Djurkic
# 9/12/2018
import csv

# listMatch takes in a value to search for(desire) and a file name to load (file)
# the function then searches row by row for this index value and when found returns a list with the value removed
def listMatch(desire, file):
    flist = []  # list which accepts loaded strings
    with open(file) as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        for row in readCSV:  # for every row in readCSV
            flist.append(row)  # append to flist

    for i in flist:
        if desire in i:  # if our desired string matches in i
            returnList = i  # create a list called returnList and equate it to i
    returnList.remove(desire)  # remove the string we were looking for from the list as it is used for indexing
    return returnList  # return our list!

# saveList appends a list (slist) to a row within a csv file (file)
def saveList(sList, file):
    with open(file, 'a+') as csvfile:  # open the file in append mode
        writeCSV = csv.writer(csvfile)  # we declare a variable writeCSV equal to our csv file in write mode
        writeCSV.writerow(sList)  # append a row from sList to the csv file

# as an example we input into savelist the return value of listMatch with the parameter 'Plain',
# then saveList appends it to the desired file
saveList(listMatch('Plain', 'area.txt'), 'newArea.txt')





