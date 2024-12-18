# Composition In OOP
"""
composition is a design principle where one class is used as a part of another class, forming 
a "has-a" relationship between them. This allows for building complex types by combining objects of 
other types. Composition is used to model real-world relationships between objects, where one class 
contains instances of other classes as attributes.
"""

class Engine:
    def __init__(self, horsepower: int):
        self.horsepower = horsepower
    
    def start(self):
        return "Engine starts"

class Car:
    """
    'engine: Engine': is a type hint (or annotation) indicating that the engine parameter should be an instance of the Engine class. It helps with readability and type checking but doesn’t enforce the 
    type at runtime. It’s used by tools like type checkers (e.g., mypy) to validate that the correct types are used.
    or 
    We can use 'any' here - mean 'any' return instance.
    def __init__(self, make: str, model: str, engine: any):
    """
    def __init__(self, make: str, model: str, engine: Engine):
        self.make = make
        self.model = model
        self.engine = engine  # Composition: Car "has-a" Engine
    
    def start(self):
        return f"{self.make} {self.model} with {self.engine.start()}"

# Create an instance of Engine
my_engine = Engine(horsepower=150)

# Create an instance of Car with the Engine instance
my_car = Car(make="Toyota", model="Corolla", engine=my_engine)

print(my_car.start())  # Output: Toyota Corolla with Engine starts
