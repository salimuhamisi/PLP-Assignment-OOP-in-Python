#create a Car and Plane that both have a move() method but behave differently
class Vehicle:
    def move(self):
        pass  # abstract idea of movement

class Car(Vehicle):
    def move(self):
        print("Driving on the road...")

class Plane(Vehicle):
    def move(self):
        print("Flying in the sky...")

class Boat(Vehicle):
    def move(self):
        print("Sailing on the water...")

# Example usage
vehicles = [Car(), Plane(), Boat()]

for v in vehicles:
    v.move()
