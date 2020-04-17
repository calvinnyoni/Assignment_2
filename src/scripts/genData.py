#Programme to generate random subset of data from loadshedding data
#Calvin Nyoni
#4 March 2020

from random import randint

file = open(r"C:\Users\calvin.nyoni\Desktop\Assignment_2\src\Load_Shedding_All_Areas_Schedule_and_Map.clean.final.txt","r")

data = []

#get all loadshedding data
for line in file:
    data.append(line)

file.close()

#list of sample file names
listOfNSamples = ["n1","n2","n3","n4","n5","n6","n7","n8","n9","n10"]

size = 250

for sample in listOfNSamples:
    file1 = open(sample, "w+") #random lines text file
    file2 = open(sample+"Test", "w+") #corresponding random arguments
    i=0
    while i < size: #generate i lines randomly 
        randomNum = randint(0,len(data)-1)
        randomLine = data[randomNum]
        splitLine = randomLine.split()
        file1.write(randomLine) #for generating random lines
        file2.write(splitLine[0]+"\n") #for generating test arguments
        i = i + 1
    file1.close()
    file2.close()
    size = size + 250 #increase sample size with each loop
