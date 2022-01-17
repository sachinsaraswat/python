class Vehicle:
    speed =0
    
    def __init__(self):
        print ("Init")
        
    
    def accelerate(self, accelerateAmount):
        self.speed += accelerateAmount
        
        
# Main

Camry  = Vehicle()

print ("Camry Speed now :: ", Camry.speed)
Camry.accelerate(10)
print ("Camry Speed after Aceleration is :: " , Camry.speed)