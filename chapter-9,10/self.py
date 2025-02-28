class Employee:
    language = "python" # this is a class attribute
    salary = 1200000

    def getInfo(self):
        print(f"The language is  {self.language}. The salary is {self.salary}")

harry = Employee()
harry.language = "Javascript"
#harry.getInfo()
Employee.getInfo(harry)        