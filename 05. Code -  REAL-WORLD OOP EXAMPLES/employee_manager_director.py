
#  EMPLOYEE → MANAGER → DIRECTOR

# Base class: Employee
class Employee:
    def __init__(self, name, id):
        # Initialize name and ID attributes
        self.name = name
        self.id = id

    def show(self):
        # Display basic employee information
        print(f"Employee: {self.name}, ID: {self.id}")

# Derived class: Manager inherits from Employee
class Manager(Employee):
    def __init__(self, name, id, team_size):
        # Call the constructor of the Employee class using super()
        super().__init__(name, id)
        # Add additional attribute specific to Manager
        self.team_size = team_size

    def show(self):
        # Call the show method of the Employee to reuse the existing Logic
        super().show()
        # Add Manager-specific output
        print(f"Team Size: {self.team_size}")

# Derived class: Director inherits from Manager (multi-level inheritance)
class Director(Manager):
    def __init__(self, name, id, team_size, stocks):
        # Call the constructor of the Manager class using super()
        super().__init__(name, id, team_size)
        # Add Director-specific attribute
        self.stocks = stocks

    def show(self):
        # Call the show method of Manager (which also calls Employee's show)
        super().show()
        # Add Director-specific output
        print(f"Stocks: {self.stocks}")

# Create a Director object and call its show method
dir1 = Director("Shankar", "D001", 20, 5000)
dir1.show()