class Vehicle:
    speed =0
    
    def __init__(self):
        print ("Init")
        
    def __init__(self, launchSpeed =0):
        self.speed = launchSpeed 
        
    def accelerate(self, accelerateAmount):
        self.speed += accelerateAmount
        
        
# Main

Camry  = Vehicle()

print ("Camry Speed now :: ", Camry.speed)
Camry.accelerate(10)
print ("Camry Speed after Aceleration is :: " , Camry.speed)

rocketCar = Vehicle(1000)

print("Tesla Rocket Car is moving at ::" , rocketCar.speed)


del rocketCar
del Camry