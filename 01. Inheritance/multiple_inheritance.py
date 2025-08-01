
# Define the first parent class: Animal
class Animal:
    def speak(self):
        print("Animal speaks")         # Method that prints a message indicating the animal speaks

# Define the second parent class: Bird
class Bird:
    def fly(self):
        print("Bird flies")            # Method that prints prints a message that Bird flies

# Define the child class: Bat
# This class inherits from both Animal and Bird - demonstrating multiple inheritance
class Bat(Animal, Bird):               # Multiple inheritance
    def echo(self):
        print("Bat uses ecolocation")  # Method specific to Bat class

# Create an Object of the Bat class
b = Bat()

# Call the method from Animal class
b.speak()                              # Output: Animal speaks

# Call the method from Bird class
b.fly()

# Call the method defined in the Bat class
b.echo()                               # Output: Bat uses echolocation
 
