# Q: How do you define a class in Python and create an instance of that class?
# Defining a Class
class My_Class:
    def __init__(self):
        print("My_Class Named class is Defined")


# Q: How can you use inheritance to extend a class in Python?
class Parent:
    def __init__(self):
        print("Parent class is called")
        
class Child(Parent):
    def __init__(self):
        # Parent.__init__(self)
        super().__init__()
        print("Child class is called")
        
        
# Q: How do you use encapsulation to hide data within a class?
        # through the use of access modifiers such as private, protected, and public
class Encapsulation:
    class Parent:
        def __init__(self):
            self.place = "ABC"
            self._age = 20
            self.__name = "XYZ"
        def display(self):
            print(self._age)
            print(self.__name)
            
    class Child(Parent):
        def __init__(self):
            super().__init__()
        
        def Chld_display(self):
            print(self._age)
            # print(self.__name)
            
# Q: How does polymorphism work in Python, and how can you implement it?
class Polymorphism:
    class Bird:
        def intro(self):
            print("There are so many types of Birds.")
        def fly(self):
            print("Most of the Birds can fly but some cannot.")
            
    class sparrow(Bird):
        def fly(self):
            print("The Sparrow can fly.")
            
    class ostrich(Bird):
        def fly(self):
            print("The Ostrich cannot fly.")

# Q: What are class methods and static methods, and how are they used?
    """
    A class method : is a method that is bound to the class and not the object of the class.
    They have the access to the state of the class as it takes a class parameter 
    that points to the class and not the object instance.
    """            
    
    """
    A static method : does not receive an implicit first argument. A static method 
    is also a method that is bound to the class and not the object of the class. 
    This method can't access or modify the class state. It is present in a class 
    because it makes sense for the method to be present in class.
    """
    """
    In general, static methods know nothing about the class state. They are utility-type 
    methods that take some parameters and work upon those parameters. On the other hand 
    class methods must have class as a parameter.
    We use @classmethod decorator in python to create a class method and we use @staticmethod decorator to create a static method in python.
    """
    
class Something:
    def __init__(self):
        print("Instance method")
        
    @classmethod
    def m1(cls,name,age):
        cls.name = name
        cls.age = age
        print(cls.name)
        
    @staticmethod
    def m2(x,y):
        z = x+y
        print(z)

# Q: How does multiple inheritance work in Python?
"""
When a class is derived from more than one base class it is called multiple 
Inheritance. The derived class inherits all the features of the base case.
"""
class Mammal:
    def mammal_info(self):
        print("Mammals can give direct birth.")

class WingedAnimal:
    def winged_animal_info(self):
        print("Winged animals can flap.")

class Bat(Mammal, WingedAnimal):
    pass
      
# Q: How do you override a method in a derived class?
class A:
    def A_method(self):
        print("This is a parent class Method..!")
class B(A):
    def A_method(self):
        print("This is a child class Method..!")

# Q: What are the __str__ and __repr__ methods used for?
"""
------------------Informal Representation (__str__)----------------------
Method: __str__(self)
Usage: Used by the print() function and str() to get a string representation of the object.
Goal: To provide a clear, concise, and informative representation of the object that is suitable for end-users.

Purpose: User-friendly, human-readable format.
Usage: Display to end-users or in print statements.
Example Output: "Alice, 30 years old"

--------------------Formal Representation (__repr__)-----------------------
Purpose: Unambiguous and detailed format suitable for debugging and development.
Usage: Development tools, debugging, and interactive interpreter.
Example Output: "Person(name='Alice', age=30)"

Method: __repr__(self)
Usage: Used by the repr() function and displayed in the interactive interpreter. It should ideally be unambiguous and could be used to recreate the object.
Goal: To provide a representation that can be used for debugging and development, often including the necessary information to reconstruct the object.

Both methods serve important roles. __str__ is used when you want a readable and 
informative string representation for end-users, while __repr__ is used to 
provide a more precise and complete description of the object for developers.
"""
class str_Representation:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def __str__(self):
        return f"My name is {self.name} I'm {self.age} year old"

    def __repr__(self):
        return f"str_Representation(name='{self.name}', age={self.age})"
        
        
# Q: How do property decorators work in Python?
"""
Decorators are a very powerful and useful tool in Python since it allows programmers 
to modify the behaviour of a function or class. Decorators allow us to wrap another 
function in order to extend the behaviour of the wrapped function, without permanently 
modifying it.
"""    
class DecoratorsFunc:
    def Decorators(func):
        def wrapper():
            print("Something Before the Decorator Function..!")
            func()
            print("Something After the Decorator Function..!")
        return wrapper
    
    # @Decorators(arguments)
    @Decorators
    def Hello():
        print("This is the Decorator function..!")
        
    # Hello()   

# Q: What is composition in OOP, and how can you implement it?
"""
In Object-Oriented Programming (OOP), composition is a design principle where a class is constructed by including instances of other classes as its attributes, rather than inheriting from them. 
This "has-a" relationship allows the composite class to leverage the functionality of its component classes, promoting modularity, flexibility, and reuse. 
By using composition, you can create complex objects by combining simpler ones, which enhances code maintainability and encapsulation.
"""
class Component: 
# composite class constructor 
	def __init__(self): 
		print('Component class object created...') 

	# composite class instance method 
	def m1(self): 
		print('Component class m1() method executed...') 


class Composite: 
	# composite class constructor 
	def __init__(self): 

		# creating object of component class 
		self.obj1 = Component() 
		
		print('Composite class object also created...') 

	# composite class instance method 
	def m2(self): 
		
		print('Composite class m2() method executed...') 

		# calling m1() method of component class 
		self.obj1.m1() 



if __name__=="__main__":
 # 1.
    # # Creating an Instance
    # obj = My_Class()
 # 2.    
    # chld = Child()
 # 3.    
    Encp = Encapsulation.Child()
    # Encp.Chld_display()
    # Encp.display()
    # print(Encp._age)
    # print(Encp.place)
 # 4.    
    Plymrpsm = Polymorphism()
    Bird = Plymrpsm.Bird()
    Sprw = Plymrpsm.sparrow()
    Ostrch = Plymrpsm.ostrich()
    
    # Bird.fly()
    # Bird.intro()
    # Sprw.fly()
    # Ostrch.fly()
 # 5.    
    # obj1 = Something()
    # Something.m1('xyz',20)
    # Something.m2(2,4)
 # 6.    
    # obj = Bat()
    # obj.mammal_info()
    # obj.winged_animal_info()
    
 # 7.
    # obj = A()
    # obj1 = B()
    # obj.A_method()    
    # obj1.A_method()
 # 8.    
    # obj = str_Representation('xyz',23)
    # print(str(obj))
    # print(repr(obj))
 # 9.    
    obj = DecoratorsFunc()
 # 10.    
    # obj = Composite()  
    # obj.m2() 