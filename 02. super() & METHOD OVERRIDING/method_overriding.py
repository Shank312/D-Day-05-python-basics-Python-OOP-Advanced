
# Allows a child class to override a method of the parent class

# Base class (Parent)
class Employee:
    def work(self):          # Base class method
        print("Employee works")

# Derived class (child)
class Manager(Employee):
    def work(self):          # Method Overriding: This replaces the Employee's work() method
        print("Manager manages") 

# Creating an object of Employee class
e = Employee()
e.work()                     # Output: Employee works
# Explanation: Since e is an instance of Employee, it calls the work() method of the Employee class.

# Creating an object of Manager class
m = Manager()
m.work()                     # Output: Manager manages

# Explanation: Since m is an instance of Manager, and Manager overrides the work() method,
# it calls the overridden version defined inside the Manager class instead of Employee's.