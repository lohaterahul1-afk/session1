# Single Inheritance in Python
class Parent:
    parentCar = "BMW"

class Child(Parent):
    childCar = "Audi"

obj = Child()
print(obj.childCar)
print(obj.parentCar)   
