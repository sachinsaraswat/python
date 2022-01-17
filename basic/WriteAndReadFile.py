#!/usr/local/bin/python3
#Open file in write mode and write to the file


outputFileName = input("Enter the FileName::" )

#outputFileNametxt="test.txt"

print (outputFileName)

outputString= input("Input the text to write:" )

outputFileHandle = open(outputFileName, "w")

outputFileHandle.write(outputString)

outputFileHandle.close()


inputFileName=input("Enter the input FileName::" )
inputFileHandle=open(inputFileName,"r")
inputString = inputFileHandle.read(100)

print (inputString)
inputFileHandle.close()