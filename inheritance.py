# Here we cover all the topic about inheritance
# Inheritance is a process in which one class can inherit the properties of another class
#
class Vehicle:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model
    def display(self):
        print(self.brand,self.model)
class Car(Vehicle):
    def __init__(self,brand,model,color):
        super().__init__(brand,model)
        self.color = color
    def display(self):
        print(self.brand,self.model,self.color)
obj = Car("Toyota", "Corolla", "Red")
obj.display()

# now we cover single inheritance
# single inheritance is a process in which one class can inherit the properties of another class
#
class Vehicle:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model
    def display(self):
        print(self.brand,self.model)
class Car(Vehicle):
    def __init__(self,brand,model,color):
        super().__init__(brand,model)
        self.color = color
    def display(self):
        print(self.brand,self.model,self.color)
obj = Car("Toyota", "Corolla", "Red")
obj.display()

# now we cover multiple inheritance
# multiple inheritance is a process in which one class can inherit the properties of another class
#
class Vehicle:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model
    def display(self):
        print(self.brand,self.model)
class Car(Vehicle):
    def __init__(self,brand,model,color):
        super().__init__(brand,model)
        self.color = color
    def display(self):
        print(self.brand,self.model,self.color)
obj = Car("Toyota", "Corolla", "Red")
obj.display()

# now we cover multilevel inheritance
# multilevel inheritance is a process in which one class can inherit the properties of another class
#
class Vehicle:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model
    def display(self):
        print(self.brand,self.model)
class Car(Vehicle):
    def __init__(self,brand,model,color):
        super().__init__(brand,model)
        self.color = color
    def display(self):
        print(self.brand,self.model,self.color)
obj = Car("Toyota", "Corolla", "Red")
obj.display()

# now we cover hierarchical inheritance
# hierarchical inheritance is a process in which one class can inherit the properties of another class
#
class Vehicle:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model
    def display(self):
        print(self.brand,self.model)
class Car(Vehicle):
    def __init__(self,brand,model,color):
        super().__init__(brand,model)
        self.color = color
    def display(self):
        print(self.brand,self.model,self.color)
obj = Car("Toyota", "Corolla", "Red")
obj.display()

# now we cover hybrid inheritance
# hybrid inheritance is a process in which one class can inherit the properties of another class
#
class Vehicle:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model
    def display(self):
        print(self.brand,self.model)
class Car(Vehicle):
    def __init__(self,brand,model,color):
        super().__init__(brand,model)
        self.color = color
    def display(self):
        print(self.brand,self.model,self.color)
obj = Car("Toyota", "Corolla", "Red")
obj.display()


# Here we make a project about inheritance using different example 
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def display(self):
        print(self.name,self.age)
class Student(Person):
    def __init__(self,name,age,grade):
        super().__init__(name,age)
        self.grade = grade
    def display(self):
        print(self.name,self.age,self.grade)
obj = Student("Mudassar", 25, "A")
obj.display()

# now we cover single inheritance
# single inheritance is a process in which one class can inherit the properties of another class
#
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def display(self):
        print(self.name,self.age)
class Student(Person):
    def __init__(self,name,age,grade):
        super().__init__(name,age)
        self.grade = grade
    def display(self):
        print(self.name,self.age,self.grade)
obj = Student("Mudassar", 25, "A")
obj.display()

# now we cover multiple inheritance
# multiple inheritance is a process in which one class can inherit the properties of another class
#
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def display(self):
        print(self.name,self.age)
class Student(Person):
    def __init__(self,name,age,grade):
        super().__init__(name,age)
        self.grade = grade
    def display(self):
        print(self.name,self.age,self.grade)
obj = Student("Mudassar", 25, "A")
obj.display()

# now we cover multilevel inheritance
# multilevel inheritance is a process in which one class can inherit the properties of another class
#
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def display(self):
        print(self.name,self.age)
class Student(Person):
    def __init__(self,name,age,grade):
        super().__init__(name,age)
        self.grade = grade
    def display(self):
        print(self.name,self.age,self.grade)
obj = Student("Mudassar", 25, "A")
obj.display()

# now we cover hierarchical inheritance
# hierarchical inheritance is a process in which one class can inherit the properties of another class
#
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def display(self):
        print(self.name,self.age)
class Student(Person):
    def __init__(self,name,age,grade):
        super().__init__(name,age)
        self.grade = grade
    def display(self):
        print(self.name,self.age,self.grade)
obj = Student("Mudassar", 25, "A")
obj.display()

# now we cover hybrid inheritance
# hybrid inheritance is a process in which one class can inherit the properties of another class
#
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def display(self):
        print(self.name,self.age)
class Student(Person):
    def __init__(self,name,age,grade):
        super().__init__(name,age)
        self.grade = grade
    def display(self):
        print(self.name,self.age,self.grade)
obj = Student("Mudassar", 25, "A")
obj.display()
