#Create a class “Programmer” for storing information of few programmers working at Microsoft. 

class Programmer:
    comapny = "Microsoft"
    def __init__(self, name, salary, pin):
        self.name = name
        self.salary = salary
        self.pin = pin

p = Programmer("Srishti", 1500000, 462022) 
print(p.name, p.salary, p.pin, p.comapny)  
r = Programmer("Rohan", 1300000, 802207)
print(r.name, r.salary, r.pin, r.comapny)     