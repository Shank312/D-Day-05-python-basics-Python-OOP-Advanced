
# Why? - To enforce method structure — like interfaces in Java/C++.

from abc import ABC, abstractmethod

# Abstract Base Class (ABC)
class Animal(ABC):
    # Abstract Method - must be overridden by any subclass
    @abstractmethod
    def sound(self):
        pass

# Concrete subclass Dog that implements the abstract method
class Dog(Animal):
    def sound(self):
        print("Bark")

# Another concrete subclass Cat that also implements the abstract method
class Cat(Animal):
    def sound(self):
        print("Meow") 

# Instantiate Dog and call sound() method
d = Dog()
d.sound()               # Output: Bark

# Instantiate Cat and call sound() method
c = Cat()
c.sound()               # Output: Meow

# Trying to create an instance of Animal directly will rise an error ❌
# Because it has an abstract method that is not implemented 
# a = Animal()  # ❌ TypeError: can't instantiate abstract class Animal with abstract method sound
