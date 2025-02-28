class Employee:
    language = "Python" # this is a class attribute
    salary = 1200000

harry = Employee()
harry.language = "Javascript" # this is an object/instance attribute
print(harry.language, harry.salary)
