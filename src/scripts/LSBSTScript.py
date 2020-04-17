#Python programme to run java commands for load shedding applications
#Calvin Nyoni
#2 March 2020

import subprocess

#Output file for tests
#file = open("LSBSTOutput.txt", "w+")

#Tests
ListOfTestArgs = [
    #Correct arguments should produces outpout
    ["1", "1", "00"], #correct output: 1
    ["2", "17", "14"], #correct output: 8, 16
    ["5", "26" , "10"], #correct output: 8, 16, 4, 12, 5
    #Incorrect arguments no output/no areas found
    ["-1", "2", "3"],
    ["5", "100", "25"],
    ["2", "4", "5723"]
]

#Compile before execution
subprocess.call(["javac", "LSBSTApp.java"])

#commmand arguments
cmdArgs = ["java", "LSBSTApp"]

#Loop for each test
for test in ListOfTestArgs:
    cmdCall = cmdArgs + test
    #file.write("Input for test\n" + test[0] + " " + test[1] + " " + test[2] + ":" + "\n" + "Output for test\n") 
    #subprocess.call(cmdCall, stdout = file)
    subprocess.call(cmdCall)


#file.close()

print("Done")