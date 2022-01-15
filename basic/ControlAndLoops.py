price =10
yr=2022
amount=100

if(yr==2022):
    if (amount ==100 and price <=10):
        print ("It is cheaper")
    else:
        print ("it is not cheaper")
else:
    print ("Year is not 2022")
        
        
        
        # For loops
        
strMsg="Hello everyone!"    
for ch in strMsg:   # <-- prints one character at a time
    print (ch)
    

for itr in range (5): # <-- 0 to 4 range.
    print (itr)

for itr in range(1,10 ,2 ): # <- start =1 , max les than 10, increment = 2
    print (itr)
    

x=0

while x <=10:
    print (x)
    x+=1  #<- shorthand notation
else :
    print ("At loop Exit.... x is" , x )