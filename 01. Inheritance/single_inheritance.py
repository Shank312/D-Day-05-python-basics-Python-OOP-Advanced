

# Base class: Employee
class Employee:
    def __init__(self, name, salary):
        # Initialize name and salary attributes
        self.name = name
        self.salary = salary

    def show(self):
        # Display employee name and salary
        print(f"Name: {self.name}, Salary: {self.salary}")

# Derived class: Manager (inherits from Employee)
class Manager(Employee):                        # This is the example of single inheritance
    def __init__(self, name, salary, department):
        # Call the parent class (Employee) constructor to initialize name and salary
        super().__init__(name, salary)
        # Add a new attribute specific to Manager: department
        self.department = department

    def show(self):
        # First call the show method of the parent class to display name and salary
        super().show()
        # Then display the department specific to the manager class
        print(f"Department: {self.department}")

# Create a manager object with name "Alice", salary 90000, and department "IT"
m1 = Manager("Alice", 90000, "IT")

# Call the show method on Manager object
# This will invoke the overridden show() method in Manager, which also calls Employee's show()
m1.show()
