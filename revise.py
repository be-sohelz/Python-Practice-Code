# def multiplication(num1, num2):
#     product=num1*num2
#     summ=num1+num2
#     if product<=1000:
#         return product
#     else:
#         return summ
# num1=70
# num2=30
# print(f"result is : {multiplication(num1,num2)}")

# previous_num=0
# for i in range(10):
#     print(f'previous number : {previous_num}  and current number {i}  and sum is {i+previous_num}')
#     previous_num=i

#Empty Or Not 
# while True:
#     t=0
#     name=input("Enter Your Name : ")
#     if name:
#         pass
#     elif t>1:
#         name=input("Enter Your Name Again... : ")        
#     else:
#         print("Enter Your Name Please... ")
#         t=t+1

#multiline statement's   
# a = 10; b = 20; c = b + a
# print(a); print(b); print(c) 

# for i in range(10):
#     if i==5:
#         break
#     print(i)

# for i in range(10):
#     if i==5:
#         continue
#     print(i)


#number guessing game
# import random
# win_no=random.randint(1,10)
# count=1
# while True:
#     guess=int(input("Please Guess An Number : "))
#     if win_no==guess:
#         print(f'You Win ...! you tried {count} times ')
#         break
#     elif win_no<guess:
#         print('too high ')
#     else:
#         print('too low')
#     count+=1

#and or operator
# age=18
# code=92
# if age==18 or code==91:
#     print('you can vote ..! ')
# else:
#     print('not eligible for vote')


#print number ushing while loop
# i=0
# while i<10:
#     print('hello world')
#     i+=1

#addition of numbers
# i=0
# total=0
# while i < 10 :
#     i+=1
#     total+=i
# print(total)

# num=input('Enter Number For Addition : ')
# i=0
# total=0
# while i < len(num) :
#     total+=int(num[i])
#     i+=1
#     print(total)

# name='sohelsohell'
# i=0
# temp=" "
# while i < len(name) :
#     if name[i] not in temp :
#         temp += name[i]
#         print(f'char  {name[i]}   :  count   {name.count(name[i])}')
#     i += 1

#addion of numbers using for loop
# total=0
# for i in range(1,11):
#     total+=i
#     print(total)

# num=input('enter a number : ')
# total=0
# for i in range(len(num)):
#     total+=int(num[i])
# print(total)

# name='sohelsohel'
# temp=''
# for i in range(len(name)):
#     if name[i] not in temp:
#         temp+=name[i]
#         print(f'char {name[i]} : {name.count(name[i])}')



# for num in range(20):
#     for i in range(num):
#         print(num,end=' ')
#     print('\n')


#Function
# def addition(a,b):
#     return a+b
# print(addition(10,20))

#input with avarage
# def avrg(a,b,c):
#     result=(a+b+c)/3
#     return result
# a=int(input("enter mark A "))
# b=int(input("enter mark B "))
# c=int(input("enter mark C "))
# print(avrg(a,b,c))

#return last char
# def last(a):
#     return a[-1]
# print(last("sohel"))

#reverse the string
# def rev(a):
#     return a[::-1]
# print(rev("Sohel"))

#odd or even
# def odd_even(a):
#     if a%2==0:
#         print("it's even")
#     else:
#         print("it's odd ")
# print(odd_even(2))


# def is_true(a):
#     return a%2==0
# print(is_true(2))


#Find Greater Number :
# def great(a,b):
#     if a>b:
#         return "a is greater"
#     else:
#         return "b is greater"
# # print(great(20,100))

# def greater(a,b,c):
#     if c>a and c>b:
#         return "c is   greater"
#     elif c>b:
#         return "c is greater"
#     else:
#         return great(a,b)
# print(greater(30,200,300))

# def palindrom(a):
#     if a == a[::-1]:
#         return "it's polindrome"
#     else:
#         return "it's not a plondrome"
# print(palindrom('soms'))

#check true false for polindroms
# def poli(a):
#     return a==a[::-1]
# print(poli('sos'))

#default parameter's 
# def info(n,age=24):
#     print(f'name is {n} and age is {age}')
# print(info('sohel'))

# number=[0,1,2,3,'four','five','six',7.0,8.0,9.0,None,True,False]
# print(number)
# print(number[-1])
# print(number[-7:-1])
# print(number[:])
# number[3]="three"
# print(number)
# number[4:7]=[4,5,6]
# print(number)
# print(number[::-1])

#list in tuple using range
# num=list(range(1,11))
# t=('one','two','three',['four',5],'six')
# t[3].extend([0,1,2,3,'four','five','six',7.0,8.0,9.0,None,True,False])
# t[3].append(num)
# print(t)

#add data to the list
# fruits=[]
# fruits.append('apple')
# fruits.append('banana')
# fruits.append('carrot')
# fruits.append('dates')
# print(fruits)

# fru=[]
# if len(fru)==0:
#     print('empty')
# else:
#     pass

# if not fru:
#     print('empty')
# else:
#     print('not empty')
    
# if fru:
#     print('not empty')
# else:
#     print('empty')

# even=[0,2,4,6,8]
# odd=[1,3,5,7,9]
# even.extend(odd)
# print(even)
# print(odd)

# even=[0,2,4,6,8]
# odd=[1,3,5,7,9]
# even.append(odd)
# print(even)


#insert() data insert using index number
# number=[0,1,2,3,'four','five','six',7.0,8.0,9.0,None,True,False]
# number.insert(14,'Binary')
# print(number)

#pop method 
# number=[0,1,2,3,'four','five','six',7.0,8.0,9.0,None,True,False]
# popped1=number.pop()
# popped2=number.pop(4)
# print(popped2)

#remove() emove element
# number=[0,1,2,3,'four','five','six',7.0,8.0,9.0,None,True,False]
# number.remove('four')
# print(number)

# del[] for deleteting  
# number=[0,1,2,3,'four','five','six',7.0,8.0,9.0,None,True,False]
# del[number[5]]
# print(number)

#some method's count(),copy(),clear(),sort(),sorted()
# number=[0,1,2,3,'four','five','six',7.0,8.0,9.0,None,True,False]
# print(number.count(True))
# number_copy=number.copy()
# print(number_copy)
# print(number)
# number_copy.clear()
# print(number_copy)

# number=[8,9,11,77,0,1,2,3]
# number.sort()
# print(number)
# print(sorted(number))
# print(number)

#split and join
# user_info='sohel jagirdar'.split()
# print(user_info)

# name,age='sohel,24'.split(',')
# print(name,age)

#join list

# user=['sohel','usman','jagirdar']
# name=','.join(user)
# print(name)
# print(type(name))

# For Loop for list
# fruites=['banana','apple','mango','grapes']
# for i in fruites:
#     print(i)

# fruites=['banana','apple','mango','grapes','kiwi']
# i=0
# while i<len(fruites):
#     print(fruites[i])
#     i+=1 

# matrix=[[1,2,3],[4,5,6],[7,8,9]]
# for i in matrix:
#     for j in i:
#         print(j)

# matrix=[[1,2,3],[4,5,6],[7,8,9]]
# print(matrix[1][1])
# print(matrix[2][0])

# num=[5,8,3,9,4,8,6,5,2,1]
# def neg(n):
#     ls=[]
#     for i in n:
#         ls.append(-i)
#     return ls
# print(neg(num))


# def sqrts(num):
#     l=[]
#     for i in num:
#         l.append(i**2)
#     return l
# print(sqrts(range(1,10)))

#for loop for reverse the string 
# name=['sohel','osman','jagirdar']
# def rev(l):
#     ls=[]
#     for i in l:
#         ls.append(i[::-1])
#     return ls
# print(rev(name))

#rev list using indexing
# num=list(range(1,10))
# def rev(l):
#     return l[::-1]
# print(rev(num))
    
# number=list(range(1,10))
# def rev(l):
#     return l[::-1]
# print(rev(number))

# num=[9, 8, 7, 6, 5, 4, 3, 2, 1]
# def rev1(l):
#     ls=[]
#     for i in range(len(l)):
#         popped=l.pop()
#         ls.append(popped)
#     return ls
# print(rev1(num))

#reverse() method
# num=[9, 8, 7, 6, 5, 4, 3, 2, 1]
# num.reverse()
# print(num)


#even odd sepresion for list
# num=[9, 8, 7, 6, 5, 4, 3, 2, 1]
# def ev_odd(l):
#     eve=[]
#     odd=[]
#     for i in l:
#         if i%2==0:
#             eve.append(i)
#         else:
#             odd.append(i)
#     return [eve,odd]
# print(ev_odd(num))


#find present or not
# a=[8, 3,6, 4, 2,9]
# b=[9, 7, 5, 3, 1,4]
# def present(a,b):
#     same=[]
#     for i in a:
#         for j in b:
#             if i==j:
#                 same.append(i)
#     return same
# print(present(a,b))


#count list insides list
# lists=[1,2,3,[4,5,6],7,[8,9],10,[11,12],[13]]
# t=0
# for i in lists:
#     if type(i)== list:
#         t+=1
# print(f'count of list is : {t}')


#tuple
# example=('sohel','rabi','rifa','raeah')
# for i in example:
#     print(i)

# example=('sohel','rabi','rifa','raeah')
# i=0
# while i < len(example):
#     print(example[i])
#     i+=1

#tuple unpacking
# example=('sohel','rabi','rifa','raeah')
# n1,n2,n3,n4=example
# print(n1,n2,n3,n4)

# def unpack(a,b):
#     add=a+b
#     mul=a*b
#     return add,mul
# add,mul=unpack(2,3)
# print(add)
# print(mul)


#list inside tuple
# example=('sohel',[1,2,3,4,5],'rabi','rifa','raeah')
# example[1].insert(6,'sohel')
# ls=[]
# for i in range(len(example[1])):
#     popped=example[1].pop()
#     ls.append(popped)  
# print(example)
# print(ls)



#set 

#remove redundant values
# number=[1,1,2,2,3,4,5,5,6,8,9,8,9]
# s=set(number)
# print(s)
# num=list(s)
# print(num)

# set_demo={1,1.1,2,3,'four','five',False}
# set_demo.add('sohel')
# print(set_demo)
# set_demo.discard(False)
# print(set_demo)

#union ( | ) remove duplicates from sets
# a={1,2,3,4}
# b={3,4,5,6}
# union= a | b
# print(union)


#intersection ( & ) show same value from sets or show common values
# a={1,2,3,4}
# b={3,4,5,6}
# intr_sec= a & b
# print(intr_sec)


#Dictionary

# user={
#     'name':'sohel',
#     'age':24
# }
# print(user)

# print(user['name'])

#Dictionary method 2
# user1=dict(name='sohel',age=24,roll_mo=11)
# for i in user1:
#     print(user1[i])

#add data to empty dictionary
# user={}
# user['name']='sohel'
# user['age']=24
# user['roll']=11
# user['mob']=91
# print(user.values())
# print(user.items())

#user name

# user={
#     'name':'sohel',
#     'age':24
# }

# if 'names' in user:
#     print('yes')
# else:
#     print('No')

# if 'ages' in user.keys():
#     print('yes')
# else:
#     print('no')

# if '24' in user.values():
#     print('Yes')
# else:
#     print('No')



# cricketer={
#     'dhoni':['csk','ipl','india'],
#     'rohit':['mi','ipl','india'],
#     'kohli':['rcb','ipl','india']
# }
# print(cricketer)
# for i in cricketer.values():
#     print(i)

# for i in cricketer.items():
#     print(i)

# cricketer['shami']=['punjab','ipl','india']
# print(cricketer)

# popped=cricketer.pop('kohli')
# print(cricketer)
# print(popped)


# user={
#     'name':'sohel',
#     'age':24,
#     'class':'cse',
# }

# user1={
#     'name':'sohel jagirdar',
#     'year':3,
#     'hobby':['cricket','machine learning','data science'],
#     'purpose':'entrepreneur',
# }
# user.update(user1)
# print(user)

#dictionary overriding duplicate values
# user={
#     'name':'sohel',
#     'age':23,
#     'age':24
# }
# print(user)

#fromkeys() method  
# d=dict.fromkeys(['name','age','mob no'],'unknown')
# print(d)

# d=dict.fromkeys(['name','age','mob no'],['unknown','unknown','unknown'])
# print(d)

# names={
#     'name1':'sohel',
#     'name2':'rabi',
#     'name3':'rifa',
#     'name4':'raeah',
# }
# name=names.get('name1')
# print(name)

# if 'sohels' in names.get('name1'):
#     print('yes')
# else:
#     print('no')

#cube finder
# def cube_f(n):
#     d={}
#     for i in n:
#         d[i]=int(i)**3
#     return d
# num=input('enter number for cube : ')
# print(cube_f(num))

# def word_counter(s):
#     d={}
#     for i in s:
#         d[i]=s.count(i)
#     return d
# print(word_counter('sosohehell'))


#*args
# def all_total(*args):
#     total=0
#     for i in args:
#         total+=i
#     return total
# l=[1,2,4,5,6,7]
# print(all_total(*l))


#normal Parameter with args
# def np_with_args(num,*args):
#     print(num)
#     total=0
#     for i in args:
#         total+=i
#     return total,num**2
#     print(args)
# print(np_with_args(1,2,4,5,6,7))


#lambda functions
# a=lambda a,b: a+b
# print(a(8,2))

#lambda divisible by 2 or not 
# l=lambda a: a%2==0
# print(l(4))

#lambda
# s=lambda a: a[-1]
# print(s('sohel jr'))

#lambda function
# a=lambda a: len(a)>5
# print(a('j'))

#another way
# a=lambda a: True if len(a)>5 else False
# print(a('soheljr'))

# def mul(*args):
#     total=1
#     for i in args:
#         total*=i
#     return total
# l=[1,2,3,4,5,6,7]
# print(mul(*l))

#enumerate function --> return position and object/value
# name=['name','age',24,5,2]
# pose=0
# for i in name:
#     print(f'pose {pose}  : object {i}')
#     pose+=1

# l=['name','age',24,5,2]
# for i,j in enumerate(l):
#     print(f'position is {i} and value is {j}')


#**kwargs i.e keyword arguments
# def fun(**kwargs):
#     print(kwargs)
# fun(name='sohel',age='24')

#unpack dictionary
# def fun(**kwargs):
#     for k,v in kwargs.items():
#         print(f' key : {k} || value : {v}')
# d={'name':'sohel','age':24}
# fun(**d)


# def fun(num,age=24,**kwargs):
#     print(num) 
#     for k,v in kwargs.items():
#         print(f' key : {k} || value : {v}')
# d={'name':'sohel','age':24}
# fun(2,**d)


#if in **kwargs dictionary 'reverse==True' then reverse list element else do print as it is.  
# def fun(l,**kwargs):
#     if kwargs.get('reverse')==True:
#         for i in l:
#             return i[::-1].title()
#     else:
#         for i in l:
#             return i.title()
# name=['sohel','ahe']
# print(fun(name,reverse=True))


#Map Function 
# l=[1,2,3,4,5,6,7,8,9]
# def sqrts(a):
#     return a%2==0
# print(list(filter(sqrts,l)))

#other way using lambda
# print(list(map(lambda a: a**2,l)))

#other way using list comprehensions
# l=[i**2 for i in l]
# print(l)


# s=['sohel','usman']
# def rev(a):
#     return a[::-1]
# print(list(map(rev,s)))

#other way using lambda
# print(list(map(lambda a: a[::-1],s)))

# l=[1,2,3,4,5,6,7,8,9]
# even=filter(lambda a: a%2==0,l)
# print(list(even))


# user=['user1','user2','user3','user4']
# name=['sohel','rabi','rifa','raeah']
# print(list(zip(user,name)))


# t=[(1,'a'),(2,'b'),(3,'c')]
# print(dict(t))

# l=[(1,2,),(3,4),(5,6),(7,8)]
# l1,l2=list(zip(*l))
# print(list(l1+l2))

# l=[(1,2,),(3,4),(5,6),(7,8)]
# l1,l2=list(zip(*l))
# max_list=[]
# for pair in zip(l1,l2):
#     max_list.append(max(pair))
# print(max_list)

#all() function
# l1=[1, 3, 5, 7,2]
# l2=[2, 4, 6, 8]
# new_l=[]
# for i in l2:
#     if i%2==0:
#         new_l.append(True)
#     else:
#         new_l.append(False)
# print(any(new_l))


# l=['sohel jagirdar','s','name','age']
# def func(a):
#     return len(a)
# print(min(l,key=func))
# print(max(l,key=func))

# print(min(l,key=lambda a: len(a)))
# print(max(l,key=lambda a: len(a)))


# l=[{'name':'sohel','score':50,'age':24},
# {'name':'fifa','score':24,'age':2},
# {'name':'babu','score':21,'age':4}
# ]

# print(max(l,key=lambda a: a.get('score'))['name'])
# print(min(l,key=lambda a: a.get('score'))['name'])

# result=max(l,key=lambda a: a.get('score'))
# print(result)
# winner=result['name']
# print(winner)

# sorted function on dictionary
# event=[{'name':'sohel','score':50,'price':24000},
# {'name':'fifa','score':24,'price':2100},
# {'name':'babu','score':25,'price':201}
# ]
# print(sorted(event,key = lambda d: d['price']))

# # for reverse the dictionary price
# print(sorted(event,key = lambda d: d['price'], reverse=True))

# scores={
#     'sohel':{'score':70,'age':24},
#     'rifa':{'score':50,'age':5},
#     'rabi':{'score':52,'age':2}
# }
# print(sorted(scores,key=lambda i: scores[i]['score'],reverse=True ))


# def add(a,b):
#     return a+b
# a=add
# print(a(2,5))


#my map function
# def fun(a):
#     return a**2
# def my_map_function(fun,l):
#     s=[fun(i) for i in l]
#     return s
# l=[1,2,3,4,5,6,7,8,9]
# print(my_map_function(fun,l))


#function as arguments
# def my_map(fun,l):
#     return [fun(i) for i in l]
# l=[1,2,3,4,5,6,7,8,9]
# print(my_map(lambda a: a**2,l))


#function return function / closure
# def outer_fun():
#     def inner_fun():
#         print('this is inner function calling')
#     return inner_fun
# v=outer_fun()
# v()

#outer funtion with massage
# def outer(msg):
#     def inner():
#         print(f'this is the massage : {msg}')
#     return inner
# v=outer('hello from sohel')
# v()

# def power(n,p):
#     def number():
#         print(n**p)
#     return number
# v=power(3,3)
# v()

# def p(x):
#     def n(n):
#         return n**x
#     return n
# v=p(3)
# print(v(3))



# def g():
#     print("Hi, it's me 'g'")
#     print("Thanks for calling me")  
# def f(func):
#     print("Hi, it's me 'f'")
#     print("I will call 'func' now")
#     func()    
#     print("func's real name is " + func.__name__)
# f(g)

# def decor_func(any_func):
#     def wrap_func():
#         print('This is wrapper function1')
#         any_func()
#         print('This is wrapper function2')
#     print('this is decor_func')
#     return wrap_func
# def func1():
#     print('this is any_func')
# v=decor_func(func1)
# v()

# @decor_func
# def func2():
#     print('this is func2 ')
# func2()


# import time
# import math
# def outer(func):
#     def inner(*args,**kwargs):
#         begin=time.time()
#         func(*args,**kwargs)
#         end=time.time()
#         print("Total time taken in : ", end - begin)
#     return inner
# @outer
# def func1():
#     time.sleep(2) 
# # func1()

# @outer
# def func2(a,b):
#     print((a+b)**2)
# a,b=1,2
# func2(a,b)

# def outer(func):
#     def inner(*args,**kwargs):
#         s=[]
#         for i in args:
#             s.append(type(i)==int)
#         if all(s):
#             return func(*args,**kwargs)
#         return 'all element are not same type'
#     return inner
# @outer
# def add(*l):
#     total=0
#     for i in l:
#         total+=i
#     return total
# l=[1,2,3,4,5,6,7,8,'9']
# print(add(*l))

# def check_data(data_type1,data_type2):
#     def outer(func):
#         def inner(*args,**kwargs):
#             s=[]
#             for i in args:
#                 s.append(type(i)==data_type1 or data_type2)
#             if all(s):
#                 return func(*args,**kwargs)
#             return 'not same datatype'
#         return inner
#     return outer
# @check_data(int,float)
# def name(*l):
#     total=0
#     for i in l:
#         total+=i
#     return total
# l=[1,2,3,4,5,6.6,7,8.2,7]
# print(name(*l))


#Generator -->fast,eficient,time and memory saving,iterable only ones, create using 'yield' keyword
# def num(n):
#     for i in range(1,n+1):
#         yield i
# for i in (num(10)):
#     print(i)

# def num(n):
#     for i in range(1,n+1):
#         yield i**2
# for i in num(100):
#     print(i)

# y=(i**2 for i in range(100000))
# for i in y:
#     print(i)

# import time
# begin=time.time()
# l=(i**2 for i in range(1,1000000))
# end=time.time()
# print(end-begin)

# def my_map(*n):
#     li=[i**2 for i in n]
#     yield li
# l=[1,2,3,4,5,6]
# var=my_map(*l)
# print(var)
# for i in var:
#     print(i)


# def my_map(func,*args):
#     s=[]
#     for i in args:
#         s.append(func(i))
#     yield s
# l=[1,2,3,4,5,6]
# var=my_map(lambda a: a**2,*l)
# print(var)
# for i in var:
#     print(i)


# class Person:
#     def __init__(self,name,age):
#         self.person_name=name
#         self.person_age=age
#         print('Constructor Called..')
# p1=Person('sohel',23)
# p2=Person('jr',22)
# print(p1.person_name)
# print(p2.person_age)


#class
# class User:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age

#     def u_age(self):
#         return self.age>18

# u1=User('sohel',24)
# # print(u1.name)

# u2=User('so',17)
# print(u2.u_age())



# class Student:
#     def __init__(self,name,no,city):
#         self.name=name
#         self.no=no
#         self.city=city

#     def state(self):
#         if self.city=='Latur':
#             return 'City State is Maharashtra'

# s1=Student('sohel',11,'Latur')
# # print(s1.name)
# print(s1.state())


# class Mobile:
#     dis=10
#     def __init__(self,model,price):
#         self.model=model
#         self.price=price
#     def discount(self):
#         disc=self.price-self.price*self.d/100
#         return disc

# m1=Mobile('nokia',20000)
# m2=Mobile('LG',25000)
# m2.dis=50
# # print(m1.price)
# print(m2.discount())



#class variable
# class Circle:
#     pi=3.14    #'''class object'''
#     def __init__(self,radius):
#         self.radius=radius

#     def area(self):
#         area=Circle.pi*self.radius**2
#         return area

#     def circumfrence(self):
#         circumf=2*Circle.pi*self.radius
#         return circumf
    
# c1=Circle(3)
# print(c1.circumfrence())



#inheritance (simple)

# class Phone: ##parent class
#     def __init__(self,brand,model,price):
#         self.brand=brand
#         self.model=model
#         self.price=price
#     def info(self):
#         return f'brand is {self.brand} model is {self.model} at price {self.price}'
#     def call(self,num):
#         print(f'callig {num} .....')
#         return 'call ended'

# class Smartphone(Phone): ##cild class
#     def __init__(self,brand,model,price,memory,camera,os):
#         super().__init__(brand,model,price)
#         self.memory=memory
#         self.camera=camera
#         self.os=os
#     def smartinfo(self):
#         return f'memory is {self.memory} and camera is {self.camera}'

# s1=Smartphone('ASUS','A9',18000,'8gb','18 MP','OREO')
# # print(s1.info())
# print(s1.call('+91-8329108070'))



#multilevel inheritance

# class Phone:
#     def __init__(self,brand,model,price):
#         self.brand=brand
#         self.model=model
#         self.price=price
#     def info(self):
#         return f'brand is {self.brand} model is {self.model} at price {self.price}'
#     def call(self,num):
#         print(f'callig {num} .....')
#         return 'call ended'

# class Smartphone(Phone):
#     def __init__(self,brand,model,price,memory,camera,os):
#         super().__init__(brand,model,price)
#         self.memory=memory
#         self.camera=camera
#         self.os=os
#     def smartinfo(self):
#         return f'memory is {self.memory} and camera is {self.camera}'

# class Smartphone2(Smartphone):
#     def __init__(self,brand,model,price,memory,camera,os,cpu):
#             super().__init__(brand,model,price,memory,camera,os)
#             self.cpu=cpu
#     def smartinfo2(self):
#         return f'cpu is {self.cpu} '

# p1=Phone('nokia',1000,1500)
# print(p1.info())

# s1=Smartphone('1+',5,120000,'8GB','12mp','android')
# print(s1.info())

# s2=Smartphone2('1+',5,120000,'8GB','12mp','android','SnapDragon - 856')
# print(s2.smartinfo2())



#Multilevel inheritance prta

# class A:
#     def __init__(self,name):
#         self.name=name
#     def names(self):
#         print(f'calling from "A" & name is {self.name}')
# class B(A):
#     def __init__(self,name,age):
#         super().__init__(name)
#         self.age=age
#     def ages(self):
#         print(f'calling from "B" & name {self.name} age is {self.age}')
# class C(B):
#     def __init__(self,name,age,city):
#         super().__init__(name,age)
#         self.city=city
#     def cities(self):
#         print(f'calling from a & name {self.name} age is {self.age} from city {self.city}')

# a1=A('sohel')
# b1=B('sohel',24)
# c1=C('sohel',24,'latur')

# print(a1.names())

# print(b1.ages())
# print(b1.names())

# print(c1.names())
# print(c1.ages())
# print(c1.cities())


#multiple inheritance 

# class A:
#     def __init__(self,name):
#         self.name=name
#     def names(self):
#         print(f'calling from "A" & name is {self.name}')
# class B(A):
#     def __init__(self,name,age):
#         super().__init__(name)
#         self.age=age
#     def ages(self):
#         print(f'calling from "B" & name {self.name} age is {self.age}')
# class C(A):
#     def __init__(self,name,city):
#         super().__init__(name)
#         self.city=city
#     def cities(self):
#         print(f'calling from a & name {self.name}  from city {self.city}')
# a1=A('sohel')
# b1=B('sohel',24)
# c1=C('sohel','latur')

# print(a1.names())
# print(b1.ages())
# print(c1.cities())





#Raise Error and Exeption Handling


# def add(a,b):
#     if (type(a)==int and type(b)==int):
#         return a+b
#     raise TypeError('wrong data type given')
# print(add(5,'4'))


# class Animal:
#     def __init__(self,name):
#         self.name=name
#     def sound(self):
#         raise NotImplementedError('You Must Implement This Method In your class, not Inherited')
# class Cat(Animal):
#     def __init__(self,name,breed):
#         super().__init__(name)
#         self.name=name
#         self.breed=breed
#     def sound(self):
#         return 'Meow Meow'
# class Dog(Animal):
#     def __init__(self,name,breed):
#         super().__init__(name)
#         self.name=name
#         self.breed=breed
#     def sound(self):
#         return 'Bhoww Bhoww'

# c1=Cat('phibie','Persian')
# print(c1.sound())

# d1=Dog('jazz','Pibull')
# print(d1.sound())


# def add(a,b):
#     if (type(a)==int and type(b)==int):
#         return a+b
#     else:
#         raise TypeError('entered Wrong Data type')
# print(add(2,'3'))

# class Mobile:
#     def __init__(self,name):
#         self.name=name
    

# class Smartphone:
#     def __init__(self):
#         self.mobilestore=[]  

#     def mobile(self,new_mob):
#         if isinstance(new_mob,Mobile):
#             self.mobilestore.append(new_mob)
#         else:
#             raise TypeError('Object Must Be Instance Of Mobile Class')

# onepluse=Mobile('OnePlus 5')
# smart=Smartphone()
# print(smart.mobile(onepluse))
# phones=smart.mobilestore
# print(phones[0].name)


#exeption handling try, catch, exept:

# while True:
#     try:
#         age=int(input('Enter An Number : '))
#         break
#     except ValueError:
#         print('wrong data entred ... please try again')
#     except:
#         print('Something Is Wrong ....')
# if age > 18 :
#     print('You Are Eligible !')
# else:
#     print('You Are Under Age !')


#else , finaly block
# while True:
#     try:
#         age=int(input('Enter Your Age : '))
#     except ValueError:
#         print('Enter Wrong Datatype... Try Again')
#     except:
#         print('Something is Wrong ..')
#     else:
#         if age>18:
#             print('Eligible')
#         else:
#             print('Not Eligible')
#         break
#     finally:
#         print(f'Age is {age}')

# def div(a,b):
#     try:
#         d=a/b
#     except ValueError:
#         print('wrong Datatype Entered..')
#     except:
#         print('something is wrong')
#     else:
#         return d
# print(div(10,2))



#Custom Exeption Error

    # class NameTooShortError(ValueError):
    #     pass

    # def validate(name):
    #     if len(name) < 5:
    #         raise NameTooShortError('Name Too Short..')
    # print(validate('sohe'))
    

    #this is my new code 
    
    #My Py
def new_add(a,b):
    return a+b
print(new_add(8,2))



##new lambda
#len(string) >5 print -->True  lambdaa

fun=lambda s: len(s)>5
print(fun('jagirdar'))

#if else in normal function 
def funs(s):
    if len(s)>5:
        return True
    return False
print(funs('sohel jagirdar'))