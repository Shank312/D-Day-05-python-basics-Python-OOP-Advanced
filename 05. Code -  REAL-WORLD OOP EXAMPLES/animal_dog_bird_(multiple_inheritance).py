
#  ANIMAL → DOG, BIRD (Multiple Inheritance)

# Base class: Animal
class Animal:
    def eat(self):
        print("Eats food")                  # Common behaviour for all animals

# First derived class: Dog (inherits from Animal)
class Dog(Animal):
    def sound(self):
        print("Barks")                      # Specific behaviour for Dog

# Second derived class: Bird (inherits from Animal) 
class Bird (Animal):
    def fly(self):
        print("Flies in sky")               # Specific behaviour for Bird

# Hybrid class using Multiple Inheritance: inheritance from both Dog and Birds
class Hybrid(Dog, Bird):                    # Inherits all methods from Dog, Bird and Animal
    def show(self):
        # Calling inherited methods 
        self.eat()                          # From Animal
        self.sound()                        # From Dog
        self.fly()                          # From Bird

# Create object of Hybrid class
hybrid = Hybrid()

# Call the show() method, which internally calls multiple inherited methods
hybrid.show()
