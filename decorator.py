#Function in as variable--> we can store function in variable
# def add(a,b):
#     return a+b
# a=add
# print(a(2,3))          


#map() function take function as argument --> map is iterator
# l=[1,2,3,4]
# def fun(a):
#     return a**2
# print(list(map(fun,l)))

#map() using lambda
# l=[1,2,3,4]
# print(list(map(lambda a: a**2,l)))

#creating our own function wich take function as argument
#creating own map function using function
# def fun(a):
#     return a**2
# def my_map_func(func,l):
#     sqr_list=[]
#     for i in l:
#         sqr_list.append(fun(i))
#     return sqr_list
# l=[1,2,3,4]
# print(my_map_func(fun,l))



#same fuction using list comprehenssion
# def fun(a):
#     return a**2
# def my_fun(func,l):
#     return [fun(i) for i in l]
# l=[1,2,3,4]
# print(my_fun(fun,l))


#function as argument using lambda
# def my_map(fun,l):
#     l2=[]
#     for i in l:
#         l2.append(fun(i))
#     return l2
# l=[1,2,3,4]
# print(my_map(lambda a: a**2,l))



#function return function / closure
# def outer_func():
#     def inner_func():
#         print('this massage from inner function')
#     return inner_func
# v=outer_func() """ outer_func() return inner fuction, not return msg of inner function """
# v()            """ v() print massge of inner funtion"""


#outer func return msg of inner function /closure
# def outer(msg):
#     def inner():
#         print(f'massage is {msg} ')
#     return inner
# v=outer('hello work hard')   #"""outer function return inner function"""
# v()                         #"""v() execute inner function """



#finding multiple power of number by using funtion return fintion/closure
# def power(x):
#     def num(n):
#         return n**x
#     return num
# num=power(2)  
# print(num(2))
# cube=power(3)
# print(cube(3))


"""
-decorator inhance the functionality of function
-'@' used to assign decorator with function (@decorator_function)
-@ is also called senthetic sugar  
-must add *args,**kwargs in decorators function
-must return function given to the decorator
"""
# def decorator_fun(any_func):
#     def wrapper_fun():
#         print('this is decorator function')
#         any_func()
#     return wrapper_fun
# def fun1():
#     print('this is its func1 awosome')
# v=decorator_fun(fun1)
# v()


#calling function by "@" or senthetic sugar method

# @decorator_fun
# def func2():
#         print('this is its func2 awosome')
# func2()


#decorator function with *args and *kwargs

# def decorator(func):
#     def wrapper_fun(*args,**kwargs):
#         print('this is from decorator')
#         return func(*args,**kwargs)
#     return wrapper_fun

# @decorator
# def hello(a):
#     print(f'argument from hello function')
# hello(5)

# @decorator
# def return_func(a,b):
#     return a,b
# print(return_func(5,6))




#define decorator function take 2 num as input and return operation of fuction

# def decorator(fun):
#     def wrapper_fun(*args,**kwargs):
#         print('you are calling add ()')
#         return fun(*args,**kwargs)
#     return wrapper_fun
# @decorator
# def add(a,b):
#     return a+b
# print(add(5,5))



#define decorator that can calculate the time for executuin of function
# import time
# def time_cal_decorator(func):
#     def wrapper(*args,**kwargs):
#         begin=time.time()
#         print('helloworld')
#         return_func=func(*args,**kwargs) 
#         endt=time.time()
#         print(endt-begin)
#         return return_func
#     return wrapper
# @time_cal_decorator
# def sqr(l):
#     return [i**2 for i in l]
# l=list(range(1,100))
# print(sqr(l))


#decorator to check all datatype is similar or not
# def allow_int(func):
#     def wrapper(*args,**kwargs):
#         l=[]
#         for num in args:
#             l.append(type(num)==int)
#         if all(l):
#             return func(*args,**kwargs)
#         print('enter wrong data')
#     return wrapper

# @allow_int
# def totals(*args):
#     total=0
#     for i in args:
#         total+=i
#     return total
# l1=[1,2,4,3,5,8,[5]]
# print(totals(*l1))



#decorator allow given datatype

# def allow_datatype(data_type):
#     def decorator(func):
#         def wrapper(*args,**kwargs):
#             d=[]
#             for i in args:
#                 d.append(type(i)==data_type)
#             if all(d):
#                 return func(*args,**kwargs)
#             else:
#                 print('data type not currect')
#         return wrapper
#     return decorator      
# @allow_datatype(str) ##allow type of data like str,int,float          
# def in_data(*args):  ##function allow to concadinate string
#     string=''
#     for char in args:
#         string+=char
#     return string
# l_string=['sohel','jagirdar']
# # print(in_data(*l_string))


# @allow_datatype(int) ##allow type of data like str,int,float          
# def in_data2(*args):  ##function allow to add numbers
#     total=0
#     for num in args:
#         total+=num
#     return total
# l_num=[1,2,4,5,3,6,7]
# print(in_data2(*l_num))