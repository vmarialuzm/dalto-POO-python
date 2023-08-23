class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
    
    def mostrar(self):
        print(f'Vehicle Name: {self.name} Volvo Speed: {self.max_speed} Mileage: {self.mileage}')
    
    def seating_capacity(self, capacity):
        return f"The seating capacity of a {self.name} is {capacity} passengers"

class Bus(Vehicle):
    def __init__(self, name, max_speed, mileage):
        super().__init__(name, max_speed, mileage)
    

bus = Bus("bus", 180, 12)
print(bus.seating_capacity(50))