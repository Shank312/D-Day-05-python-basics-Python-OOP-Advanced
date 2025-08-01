
# Define a class called Vector
class Vector:
    # Constructor to initialize the x and y coordinates
    def __init__(self, x, y):
        self.x = x                     # Assign the x value
        self.y = y                     # Assign the y value

    # Define how the '+' operator should behave for vector objects
    def __add__(self, other):
        # Return a new Vector object whose x and y are the sum of the two Vector's x and y
        return Vector(self.x + other.x, self.y + other.y)
    
    # Define how the object is displayed when printed
    def __str__(self):
        # Return a string representation of the Vector object
        return f"Vector ({self.x}, {self.y})"
    
# Create first Vector object with coordinates(2, 3)
v1 = Vector(2, 3)

# Create second Vector object with coordinates(1, 4)
v2 = Vector(1, 4)

# Add v1 and v2 using the overloaded "+" operator
# This calls v1.__add__(v2), which returns a new Vector(3, 7)
print(v1 + v2)                              # Output: Vector(3, 7)