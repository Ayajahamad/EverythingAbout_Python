# Class: A class is a Blueprint for creating objects. It defines the properties (attributes) and behaviors (methods) that objects of the class will have. Classes are defined using the class keyword.

class Car():

    # Attributes of class 
    wheel = 4

    # Constructor Method
    def __init__(self,model,color):
        self.model = model
        self.color = color
    
    # Method
    def Drive(self):
        return f"Car model is {self.model} and Color is {self.color}"
    
# Object: An object is an instance of a class. It is a concrete entity created based on the class blueprint.
    
# Creating Object of the CAR class
obj1 = Car(1994,"Red")
obj2 = Car(2024,"Blue")

# Attributes: Attributes are data stored inside a class or instance. They represent the state or characteristics of the object.

# Accessing the Attributes from car class.
print(obj1.color, obj1.model)
print(obj2.color, obj2.model)
print(obj1.wheel)
print(obj2.wheel)

# Methods: Methods are functions defined within a class. They define the behavior of the objects.

# Accessing Methods from Car class.
print(obj1.Drive())
print(obj2.Drive())

# Constructor (__init__): The __init__ method is a special method used for initializing objects. It is called automatically when a new instance of the class is created.