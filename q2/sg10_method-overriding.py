class Animal: # creates the superclass, Animal
  def __init__(self,name): 
    self.name = name # the only attribute
    #example of Animal methods, not used in the testing tho
  def eat(self):
    print(f"{self.name} eats beans.")
  def make_sound(self):
    print(f"{self.name} exclaims loudly.")

class Lion(Animal): #  Lion subclass
  def __init__(self,name): # for all subclasses, they inherit the name attribute
    super().__init__(name)
    #methods
  def eat(self):
    print(f"{self.name} eats fresh meat")
  def make_sound(self):
    print(f"{self.name} roars loudly!")

class Elephant(Animal):
  def __init__(self,name):
    super().__init__(name)
    #methods
  def eat(self):
    print(f"{self.name} eats grass and fruits")
  def make_sound(self):
    print(f"{self.name} trumpets!")

class Monkey(Animal):
  def __init__(self,name):
    super().__init__(name)
    #methods
  def eat(self):
    print(f"{self.name} eats bananas")
  def make_sound(self):
    print(f"{self.name} chatters!")

##testing different objects
lion = Lion("Melus")
elephant = Elephant("Reval")
monkey = Monkey("Roman")

zoo = [lion,elephant,monkey] #puts the animals into a 'zoo' aka a list

for i in zoo: #loop for the zoo display
  print(i.eat())
  print(i.make_sound())
  print("\n ---- ")
