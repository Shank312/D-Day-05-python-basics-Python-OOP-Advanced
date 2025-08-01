
# Define a class Dog with a method sound
class Dog:
    def sound(self):
        print("Bark")                     # Dog's version of sound

# Define a class Cat with method a method sound
class Cat:
    def sound(self):
        print("Meow")                     # Cat's version of sound

# A function that takes any object and calls its sound method
def make_sound(animal):
    animal.sound()                        # This demonstrate polymorphism: same interface, different behaviour

# Call make_sound with a Dog instance
make_sound(Dog())                         # Output: Bark

# call make_sound with a Cat instance
make_sound(Cat())                         # Output: Meow
