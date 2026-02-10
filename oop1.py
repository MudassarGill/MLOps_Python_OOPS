# Here we write our class and object code
class employee:
    def __init__(self):# these called dunder method or constructor
        self.name = "Mudassar"
        self.age = 20
        self.salary = 50000
    def show(self):
        print(f'Employee name is {self.name}')
        print(f'Employee age is {self.age}')
        print(f'Employee salary is {self.salary}')

# now we create object
emp1 = employee()
emp1.show()
    
class Car:
        #class attribute
        vechile_type="Four wheelers"
        def __init__(self,brand,model,year):
            self.brand = brand
            self.model = model
            self.year = year
        def show(self):
            print(f'Car brand is {self.brand}')
            print(f'Car model is {self.model}')
            print(f'Car year is {self.year}')

# now we create object
car1 = Car("Toyota", "Corolla", 2022)
car1.show()

class student:
    def __init__(self,name,age,grade):
        self.name = name
        self.age = age
        self.grade = grade
    def show(self):
        print(f'Student name is {self.name}')
        print(f'Student age is {self.age}')
        print(f'Student grade is {self.grade}')

# now we create object
student1 = student("Mudassar", 20, "A")
student1.show()
    
class Mobile:
    def __init__(self,brand,model,year):
        self.brand = brand
        self.model = model
        self.year = year
    def show(self):
        print(f'Mobile brand is {self.brand}')
        print(f'Mobile model is {self.model}')
        print(f'Mobile year is {self.year}')

# now we create object
mobile1 = Mobile("Samsung", "Galaxy S21", 2022)
mobile1.brand = "Apple"
mobile1.show()