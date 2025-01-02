class Employee:
    language = "python"
    salary = 1200000

    # The __init__ method (constructor) is defined inside the class with correct indentation.
    def __init__(self, name, language, salary):#dunder method which calls the function automatically i.e its output wil be directly printed
        self.name = name    
        self.language = language    
        self.salary = salary    

# Creating an instance of the Employee class
harry = Employee("harry", "javascript", 1300000)

# Printing the attributes of the instance 'harry'
print(harry.name, harry.language, harry.salary)
