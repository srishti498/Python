# Create a class with a class attribute a; create an object from it and set ‘a’ 
# directly using ‘object.a = 0’. Does this change the class attribute?

class Demo:
    a = 4

O = Demo()
print(O.a) # prints the class attribute because instance attribute is not present
O.a = 0 # instance attribute is set
print(O.a)# prints the instance attribute because instance attribute is present
print(Demo.a) # prints the class attribute