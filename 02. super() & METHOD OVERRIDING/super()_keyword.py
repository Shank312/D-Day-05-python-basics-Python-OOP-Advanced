
# Used to call methods from the parent class — especially in constructor chaining.

# Base class: Employee
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def show(self):
        print(f"Name: {self.name}")
        print(f"Salary: ₹{self.salary}")

# Subclass of Employee: Manager
class Manager(Employee):
    def __init__(self, name, salary, department):
        # Call the constructor of the Employee to initialize name and salary
        super().__init__(name, salary) 
        self.department = department

    def show(self):
        # Call Employee's show method
        super().show()
        print(f"Department: {self.department}")

# Subclass of Manager: Director
class Director(Manager):
    def __init__(self, name, salary, department, shares):
        # Call Manager's constructor to initialize name, salary, department
        super().__init__(name, salary, department)
        self.shares = shares                                # Additional property unique to Director

    def show(self):
        # Call manager's show method (which also calls Employee's show)
        super().show()
        # Print Director-specific info
        print(f"Shares: {self.shares}")

# Create a Director object
d1 = Director("Bob", 120000, "R&D", 5000)

# Call the show method to display all information
d1.show()