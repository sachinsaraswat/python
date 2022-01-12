#Types of variables in Python

wineAge=4        # Integer
winePrice=99.99   # Float
wineName="Douro" # String 

print("Wine Name  ::" , wineName)
print("Wine Age   ::" , wineAge)
print("Wine Price ::" , winePrice)



#String as array - 0 1 2 

print(wineName[2])  # character at index =2 

print(wineName[1:4]) # characters starting at index =1 and  till index =3

# Lists
mixedList = [ 'Apple', 'Python', 3 , 3.9 ] 

print(mixedList)
print(mixedList[1], mixedList[3])


# Tuple

mixedTuple= ( 'Apple', 'Python', 3 , 3.9 )

# Tuple are immutable, cannot change once created

print (mixedTuple)
# mixedTuple[2] ="C++"  -- TypeError: 'tuple' object does not support item assignment


# dictionary - List of key value pair

priceDict ={ "Orange" : 15}

priceDict["Apple"] =10
priceDict["Banana"]=20

print (priceDict)
print (priceDict.keys())
print (priceDict.values())



# Data type conversion

applePricePerLB = 8.99
applePricePerLBInt=  int(applePricePerLB)

print (applePricePerLBInt)