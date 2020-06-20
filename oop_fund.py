"""
#Encapsulation: 
-wrapping data and method togather that work on same unit
-Gathering data togather at on place in class is called encpsulation
-realtime eg: a company with sales dept. ,finance dept. wich keep record related there dept,
now finace dept need data of sales dept. of previous month then it can't access that data
directly, first they need to cantact and request to sales officers, then they can provide data.

#Abstaction:
-Hiding unnessesary data from user.
-a function could have huge data inside it, but it hide it and provide only functionalty to user.
-eg. in python we use sort() method wich is work on tim sort algorithm , we can use sort() directly
without writing any algorithm.in other word sort() function abstract data and provide functionality.
-realtime eg: we use API in our class method user can perform task on it without worrying about API's.

#naming convention:
-eveything is public in python 
-when we add single underscore '_' then it become protected member 
#name mangling:
-(not convenction) when we add double underscore'__' before name then member become private belong to one class only
-"__name__" this is called Dunder or magic methods
"""
#Encapsulation,Abstraction,Name Convenction,Name Mangling,Dunder/magical methods
# class Laptop:
#     def __init__(self,name,price):
#         self.nam=name
#         self._price=price
#     def discount(self):
#         return self._price
# l=Laptop('lenovo',30000)
#protected member not private
# print(l._price)
# l._price=2500
# print(l._price)

#private member 
# class Laptop:
#     def __init__(self,name,price):
#         self.name=name
#         self.__price=price ##__price is only used inside class not outside , we use _Laptop__price for use this outside the class.
#     def discount(self):
#         return self.__price
# l=Laptop('lenovo',30000)
# print(l.discount())
#we use data discriptor/dict method
# print(l.__dict__)
#we can add _classname__privatemember
#eg.
# print(l._Laptop__price)



"""
-property decorator
-negative price getter and setter
"""
class Mobile:
    def __init__(self,brand,model,price):
        self.brand=brand
        self.model=model
        # if price>0:
        #     self._price=price
        # else:
        #     self._price=0
        self._price=max(price,0)
    @property
    def info(self):
        return f'brand is {self.brand} price is {self._price}' 
    @property
    def price(self):
        return self._price
    @price.setter
    def price(self,price):
        return max(price,0)   
m1=Mobile('nokia','1100',-5000)
print(m1.info)
m1.price=-1000
print(m1.price)
m1._price=-10
print(m1._price)

    
























