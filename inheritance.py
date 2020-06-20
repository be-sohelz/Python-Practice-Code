"""
-inheritance is concept in wich base class attribute derived in child class.
"""

#Eg:
# simple and Hierarchical inheritance

# class Phone: ##Base / Parent class
#     def __init__(self,brand,model,price):
#         self.brand=brand
#         self.model=model
#         self._price=max(price,0)
#     def info(self):
#         return f'brand is {self.brand} model is {self.model} and price is {self._price} '
# class Smartphone(Phone): ##Derived/Child Class
#     def __init__(self,brand,model,price,ram,memory,camera):
#         super().__init__(brand,model,price)
#         self.ram=ram
#         self.memory=memory
#         self.camera=camera
# class Smartphone2(Phone):##Derived/Child Class
#     def __init__(self,brand,model,price,ram,memory,camera):
#         super().__init__(brand,model,price)
#         self.ram=ram
#         self.memory=memory
#         self.camera=camera
# s1=Smartphone2('Apple','iPhone 6',30000,'3gb','132 gb','20 mpx')
# print(s1.info())
# print(s1._price)
# print(s1.ram)
# print(s1.memory)

#simple and Multilevel Inhertance
# class Phone: ##Base / Parent class
#     def __init__(self,brand,model,price):
#         self.brand=brand
#         self.model=model
#         self._price=max(price,0)
#     def info(self):
#         return f'brand is {self.brand} model is {self.model} and price is {self._price} '
# class Smartphone(Phone): ##Derived/Child Class from Phone class
#     def __init__(self,brand,model,price,ram,memory,camera):
#         super().__init__(brand,model,price)
#         self.ram=ram
#         self.memory=memory
#         self.camera=camera
# class Smartphone2(Smartphone):##Derived/Child Class from Smartphone class
#     def __init__(self,brand,model,price,ram,memory,camera,color):
#         super().__init__(brand,model,price,ram,memory,camera)
#         self.color=color
#     def color_info(self):
#         return self.brand,self.color
# s1=Smartphone2('Apple','iPhone 6',30000,'3gb','132 gb','20 mpx','Black')
# print(s1.color_info())
# print(s1.info())
# print(s1.color)
# print(s1.ram)
# print(s1.memory)    

'''
Method Resulation Order (MRO)
-MRO is order of executing programs and Function
-MRO check first function is exist in class and excute it, 
if function not in calss then it execute next parent class
-when method of one class executed before another class's with same name then it's called method overridding

'''
# class Car:
#     def __init__(self,name):
#         self.name=name
#     def vehicles(self):
#         return self.name 
#     def info(self):
#         return f'vehicle is {self.name} '
# class Bike(Car):
#     def __init__(self,name,model):
#         super().__init__(name)
#         self.model=model
# class Mopad(Bike):
#     def __init__(self,name,model,price):
#         super().__init__(name,model)
#         self.price=price
#     def info(self):
#         return f'name {self.name} and price is {self.price}'
# c=Car('Audi')
# b=Bike('KTM', 'RX100')
# m=Mopad('Activa','4G',60000)
# print(b.name)
# print(b.info())
# print(c.info())
# print(m.info())   ##Method info() of Mopad class is executing (method overriding)
 
##isinstance() and issubclass() buildin functio
##isinstance() check its instance of class or not
# print(isinstance(c,Car))
# print(isinstance(b,Car))
# print(isinstance(b,Bike))
# print(isinstance(m,Bike)) 

# issubclass(subclass,class) check instance is of subclass or not
# print(issubclass(Car,Bike))  ##False
# print(issubclass(Bike,Bike)) ##True becouse every class is subclass of itself
# print(issubclass(Bike,Car))  ##True
# print(issubclass(Mopad,Bike)) ##True


#Multiple Inheritance 
# class A:
#     def hi(self):
#         return 'hi from class A'
# class  B:
#     def hi(self):
#         return 'hi from class B'
# class C(A,B):
#     pass
# a=A()
# b=B()
# c=C()
##we can use help() function for check Method Resulation Order (MRO)
# print(C.mro())  ##return list of class sequence
# print(a.hi())
# print(b.hi())
# print(c.hi())
# print(help(c))





