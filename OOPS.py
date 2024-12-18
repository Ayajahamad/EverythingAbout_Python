# Inheritance
class Inheritance:
    class Parent:
        def __init__(self,Family,Home):
            self.Family = Family
            self.Home = Home

    class Child(Parent):
        def __init__(self, Family, Home, Name, Age):
            self.Name = Name
            self.Age = Age
        
            # # invoking the __init__ of the parent class
            Inheritance.Parent.__init__(self,Family,Home)
            # super().__init__(Family, Home)
     
        def display(self):
            print(f"Family Name is : {self.Family}\nHome Name is : {self.Home}\nName is : {self.Name}\nAge is : {self.Age}")
        
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
            print(self.__name)



# Q: How do you define a class in Python and create an instance of that class?
# Defining a class            
class My_Class:
    print("class My_Class is defined")
# creating instance
obj = My_Class()    
     
# Q: How can you use inheritance to extend a class in Python?
# Q: How do you use encapsulation to hide data within a class?
# Q: How does polymorphism work in Python, and how can you implement it?
# Q: What are class methods and static methods, and how are they used?
# Q: How does multiple inheritance work in Python?
# Q: How do you override a method in a derived class?
            
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


         
if __name__=='__main__':
    ## Inheritance..
    
    # Inh = Inheritance.Child("Brigeds","xyz","ABC",18)
    # obj.display()


    ## Polymorphism..
    
    # Ply_brd = Polymorphism.Bird()
    # Ply_sprw = Polymorphism.sparrow()
    # Ply_ostrch = Polymorphism.ostrich()
    
    # Ply_brd.intro()
    # Ply_brd.fly()
    
    # Ply_sprw.intro()
    # Ply_sprw.fly()
    
    # Ply_ostrch.intro()
    # Ply_ostrch.fly()
    

    # # Encapsulation..
    
    # Enc = Encapsulation.Parent()
    # Enc.display()
    # print(Enc._age)
    # # print(Enc.__name)
    # # Accessing the private attribute from outside (using name mangling)
    # print(Enc._Parent__name)
    
    # Enc_Chld = Encapsulation.Child()
    # Enc_Chld.display()
    # print(Enc_Chld._age)
    
    # # String Representation
    # str_rep = str_Representation("XYZ",23)
    # str1 = str(str_rep)
    # repr1 = repr(str_rep)
    
    # # To recreate the object
    # a = eval(repr1)
    # print(a.name)

    # print(str1)
    # print(repr1)
    
    # # creating object of composite class 
    # obj2 = Composite() 
    # calling m2() method of composite class 
    # obj2.m2() 
    
    obj = My_Class()