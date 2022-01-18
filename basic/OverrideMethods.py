class Vehicle:
    speed =0
    weight =0
    
    
    def __init__(self):
        print ("Init")
        
    def __init__(self, launchSpeed =0, weight=0):
        self.speed = launchSpeed 
        self.weight = weight
        
    def accelerate(self, accelerateAmount):
        self.speed += accelerateAmount
        

class Car (Vehicle):
    make =""
    model=""
    year=""
    
    def __init__(self, launchSpeed=0, weight=0 , make ="UnKnown", model ="UnKnown", year="0"):
        super().__init__(launchSpeed, weight)
        self.make=make
        self.model=model
        self.year=year
    
    def __str__(self) -> str:
        retString= str(self.__class__.__name__) + " [Make   = " + str(self.make ) + "\nModel  = " + str(self.model)  + "\nYear   = " + str(self.year)+ "\nWeight = " + str(self.weight) + "\nSpeed  = " + str(self.speed) +"]"
        
        
        return retString
    def accelerate(self, accelerateAmount):
        self.speed += accelerateAmount * 1.2
        
# Main

Camry  = Vehicle()

print ("Camry Speed now :: ", Camry.speed)
Camry.accelerate(10)
print ("Camry Speed after Aceleration is :: " , Camry.speed)

rocketCar = Vehicle(1000)

print("Tesla Rocket Car is moving at ::" , rocketCar.speed)

prius = Car(0,300,"Toyota", "Prius 2L","2020")

print (prius    )

prius.accelerate(10)

print (prius)



del rocketCar
del Camry
del prius