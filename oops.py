"""
-class is blueprint of object
-object/insatance is variable of class
-object can perform methods of class
-'class' keyword used to define class
-according to convention class name start with capital letter
-__init___ is constructor of class
-__init__ / constructor function contain self variable and class attribute
-constructor called by each and every class object
-we use 'self' according to convention 
-self point to object of class 
"""

#writing my first class
# class Person:
#     def __init__(self,first_name,last_name,age):
#         print('__init__ constructor called')
#         self.pf_name=first_name
#         self.pl_name=last_name
#         self.p_age=age
# user1=Person('sohel','jagirdar',24)
# user2=Person('rifa','kazi',5)
# print(user1.pf_name)
# print(user2.pf_name)

#exercise
#creating laptop class
# class Laptop:
#     def __init__(self,name,model,price):
#         # print('constructor called')
#         #instance variables
#         self.lname=name
#         self.lmodel=model
#         self.lprice=price
#         self.lname_model=name+' '+model
# laptop1=Laptop('lenovo','g-50',40000)
# laptop2=Laptop('HP','A-50',30000)
# laptop3=Laptop('Dell','inspire',48000)
# print(laptop1.lname,laptop1.lmodel,laptop1.lprice)
# print(laptop2.lname_model)


"""
-instance and object is same 
-instace method is function defined inside class
-'self' is variable of object/instance
-function defined in class is called methods
-class variable also called class Attributes
"""
# class Person:
#     def __init__(self,name,last_name,age):
#         ##instance variables
#         self.name=name
#         self.last_name=last_name
#         self.age=age
#     def fullname(self):
#         return self.name + " " + self.last_name
#     def is_18(self):
#         return self.age>=18

#calling fullname() function
# p1=Person('sohel','jagirdar',24)
# print(p1.fullname())

#calling is_18() function
# print(p1.is_18())

#we can also use 
# print(Person.fullname(p1))



#apply discount formula(discount=price-price*discount/100) or [discount=p-p*d/100]
# class Laptop:
#     def __init__(self,name,price):
#         self.nam=name
#         self.price=price
#     def discount(self,d):
#         discount=self.price-self.price*d/100
#         return discount
# l=Laptop('lenovo',30000)
# l2=Laptop('hp',40000)
# l3=Laptop('Dell',50000)
# print(l.discount(10))
# print(Laptop.discount(l,10))
# print(l2.discount(10))
# print(l3.discount(10))

#apply discount with class variable for all laptops
# class Laptop:
#     dis=10
#     def __init__(self,name,price):
#         self.nam=name
#         self.price=price
#     def discount(self):
#         discount=self.price-self.price*Laptop.dis/100
#         return discount
# Laptop.dis=0    ##laptop discount set to zero(0)
# l=Laptop('lenovo',30000)
# l2=Laptop('hp',40000)
# l3=Laptop('Dell',50000)
# print(l.discount())
# print(l2.discount())
# print(l3.discount())



#apply diff discount  for a laptop (eg. 50% off for Dell laptop only)
#in this program class check that object of class have "self" variable or not
#if class object have variable then its variable is used
# class Laptop:
#     dis=10
#     def __init__(self,name,price):
#         self.nam=name
#         self.price=price
#     def discount(self):
#         discount=self.price-self.price*self.dis/100
#         return discount
# l=Laptop('lenovo',30000)
# l2=Laptop('hp',40000)
# l3=Laptop('Dell',50000)
# l3.dis=50                 ##--> class object with its variable

# print(l.discount())
# print(l2.discount())
# print(l3.discount())

#creating class without class variable variable
# class Circle:
#     def __init__(self,redius,pi):
#         self.radius=redius
#         self.pi=pi
#     def circle_area(self):
#         return self.pi*(self.radius**2)
# c1=Circle(5,3.14)
# c2=Circle(3,3.14)
# print(c1.circle_area())
# print(c2.circle_area())


#creating class with class variable variable
# class Circle:
#     pi=3.14    ##class variable
#     def __init__(self,redius):
#         self.radius=redius
#     def circle_area(self):
#         return Circle.pi*(self.radius**2)
# c1=Circle(3)
# print(c1.circle_area())


#count class instance
# class Person:
#     var=0
#     def __init__(self,name):
#         Person.var+=1
#         self.name=name
# p1=Person('sohel')
# p2=Person('sohel')
# p3=Person('sohel')
# print(Person.var)


#class as method
#we call class name with class method
# class Person:
#     var=0
#     def __init__(self,name):
#         Person.var+=1
#         self.name=name
#     @classmethod                ##decorator
#     def count_instance(cls):
#         return f'you have created {cls.var} instances of {cls.__name__} class'
# p1=Person('sohel')
# p2=Person('sohel')
# p3=Person('sohel')
# print(Person.count_instance())

"""class as constructor topic skipped  so, do it with good resource"""
#creating class method as constructor   
# class User:
#     def __init__(self,name,last_name):
#         self.name=name
#         self.last_name=last_name
#     def fullname(self):
#         return f'{self.name}  {self.last_name}'

#     @classmethod
#     def strings(cls,string):
#         name,last_name=string.split(',')
#         return name,last_name
# u1=User.strings('sohel,jagirdar')
# print(u1.fullname())

# u=User('sohel','jagirdar')
# print(u.fullname()) 



"""
#static method
-static method is a method wich is not related to object/class
-it could have some logical connection with class
-in static method we directly return method without calling constructor
-we can call static method without object
# """
#static method 
# class User:
#     def __init__(self,name):
#         self.name=name
#     @staticmethod
#     def hello():c
#         print('hello from static method')
# u1=User('sohel')
# User.hello()

