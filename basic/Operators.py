# Arithmetic operators

print ( 2 + 4 ) # 6 
print ( 2 - 4 ) # -2 
print ( 2 / 4 ) # 0 , 0.5 ->0 int conversion
print ( 2 * 4 ) # 8
print ( 4 % 2 ) # 0 

# Comparison Operators
print (2==2) # True
print ( 3==2) # False

print ( 3!=2) # True

print ( 3 > 2) # True
print ( 3 < 2) # False
print ( 3 >=2 ) # True
print ( 3 <=2) # False

# Bitwise
x = 3  # 0000 0011
y = 2  # 0000 0010


print (x | y) # =3 
print (x  & y) # =2 
print (x ^ y) # = 1 

print ( y >>1 ) # = 1 ( 3/2 = 1.5 => 1 )

z= 32 

print (z >> 3) #  / 2 -> /2 ->/2 


# Logical - and , or

x=True
y=False

if (x and y):
    print ("it is True")
else:
    print (" It is False") # <-


if (x or y):
    print ("it is True") # <-
else:
    print (" It is False") 
    
if (x):
    print ("x is ", x)  # <-

if (not y):
    print ("Not y is :", not(y)) #<- 
    
    
    # in operator
    
    print ('H' in "Ship")
    print ('h' in "Ship")

    print ('T' in "Ship")
    print ('p' in "Ship")
    
    x =20 
    y -15
    print ("---")
    print ( x is y)
    print ( x is not y)
    
    