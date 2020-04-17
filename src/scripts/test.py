#Programme to run java commands for load shedding applications
#Calvin Nyoni
#3 March 2018

import subprocess

print("Running...")

file = open(r"C:\Users\calvin.nyoni\Desktop\Assignment_2\src\n4Test", "r")
file2 = open("values", "w+")

#subprocess.call(["javac", "LSBSTApp.java"])

#cmdArgs = ["java", "LSBSTApp"]

subprocess.call(["javac", "LSAVLTApp.java"])

cmdArgs = ["java", "LSAVLTApp"]

for line in file:
    line = line.strip('\n')
    otherArgs = line.split("_")
    cmdCall = cmdArgs + otherArgs + ["test"]
    subprocess.call(cmdCall, stdout = file2)

file.close()
file2.close()

file = open(r"C:\Users\calvin.nyoni\Desktop\Assignment_2\src\values")

results = []

for line in file:
    results.append(int(line))

avg = sum(results)/len(results)
min_value = min(results)
max_value = max(results)

print("Min ", min_value)
print("Average ", avg)
print("Max ", max_value)

print("Done")

file.close()