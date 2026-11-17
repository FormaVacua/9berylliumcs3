### ANSWERING QUESTIONS HERE

# A: What is duck typing, as explained in the video?
## Duck typing is another way of achieving polymorphism outside of inheritence. In this case, any object that resembles another object -- as long as it has the minimum requirements -- can be executed. 
## Duck typing relies on the presence of specific methods rather than by class.


#b. What did the Car class need to have so it could work inside the same loop as Dog and Cat, even if it does not inherit from the Animal class?
## The Car class needed a defined move() method. Duck typing allows the Car class to still be executed even if it's not part of the Animal hierarchy.

## 3. How does the code in 2.2 demonstrate polymorphism?
### It demonstrates that code can come in different forms. In this case, duck typing/inheritance.

class Vehicle: #creates the parent class Vehicle
  def start_trip(self): #is basically what calls each subclass since it's inherited
    return self.move()


## sub classes are made
class Car(Vehicle):
  def move(self): #each class defines a different self.move for the inherited start_trip()
    print("The car drives on the road")

class Boat(Vehicle):
  def move(self):
    print("The boat sails on water")

class Drone(Vehicle):
  def move(self):
    print("The drone flies in the sky")

vroomvroom = [Car(), Boat(), Drone()] #puts the subclasses in a list so it's easier to make outputs

for i in vroomvroom: # for every vehicle, their inherited start_trip() which leads to move() is executed
  i.start_trip()
