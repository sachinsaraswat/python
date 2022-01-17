# key: value pair

nameDict = {1 : "Apple" , 2: "Banana", 3 : "Pears"}

print (nameDict)

nameDict[0]="Orange"

print (nameDict[0])

print (nameDict)


nameDict[2]="Kiwi"

print (nameDict[2])

print (nameDict)

del nameDict[3]

print(nameDict)


# print (nameDict[3]) # Keyerror: 3 

nameDict.clear()
print(nameDict) # {}

#

indx = (1 , 2 ,3 )

sampleDict = dict.fromkeys(indx, 0)

print (sampleDict)

car = {
  "brand": "Toyota",
  "model": "Camry",
  "year": 2018
}

x = car.get("year")

print(x)


x = car.items() # Tuple for each key, value pair

print(x)

x= car.keys() # List of keys

print (x)


x= car.values() # List of values

print (x) 