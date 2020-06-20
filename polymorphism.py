'''Special magical method or Dunder method'''
# #__str__ or __repr__ for print direct output from method

# class Phone:
#     def __init__(self,brand,model):
#         self.brand=brand
#         self.model=model
#     ##we can use __str__ and __repr__ for printing value directly from it
#     ##__str__ for normal user
#     # def __str__(self):
#     #     return f'brand is {self.brand} model is {self.model}'
#     ##__repr__ for developers use 
#     def __repr__(self):
#         return f'brand is {self.brand} model is {self.model}'
#     def __len__(self):
#         return len(self.brand)
    
# p=Phone('Nokia','1100')
# print(len(p))   ##return len of string or obj or anything
# print(str(p))
# print(p)   ##we can directly call __str__ and print value


'''
-Operator overloading in python
-we use dunders to overload operator
-we can overload operators for add,sub,mul,div,and,or,xor etc.
'''
##eg.we have two object with same price and we want to add two operrators price.we use poerator overloadibg

# class Phone:
#     def __init__(self,brand,price):
#         self.brand=brand
#         self.price=price
#     ##we use operator overloadin for add,sub,mul,div,and,or,xor etc
#     def __add__(self,other):
#         return self.price + other.price
# p1=Phone('nokia',10000)
# p2=Phone('iPhone',20000)
# print(p1+p2) ##we added price of diff object


'''
Polymorphism:
-polymorphism is ability to take more than on form
-eg: len() calculate lenght for many strings,objects
-eg:'+' plus oprtor can many add int and string  
-any function or oprator can perform many task is called polymorphism
'''
##Eg 1
# 2+5=6
# 4+5=9
#'+' operator perform many task

##Eg 2
# l='sohel'
# print(len(l))
#len function can calculate len for many objects

"""
Method Overriding in python:
-if we have two or more methods with same name in multiple class then first/nearest method of class is executed
-we use method overrideing for add more feature in method/function
"""
##Method Overriding
##in this program info() method override another class's info() method

# class Phone:
#     def __init__(self,brand,model):
#         self.brand=brand
#         self.model=model
#     def info(self):
#         return self.brand,self.model
# class Smartphone(Phone):
#     def __init__(self,brand,model,ram,camera):
#         super().__init__(brand,model)
#         self.ram=ram
#         self.camera=camera
#     def info(self):
#         return f"{self.brand} model is {self.model} ram= {self.ram} cam= {self.camera}"
    
# p=Phone('Nokia','1100')
# s=Smartphone('OnePlus','6T','8Gb','32Mpx')
# print(p.info())
# print(s.info())
