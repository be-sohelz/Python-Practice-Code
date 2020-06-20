"""
-generators are iterator
-we use 'yield' keyword for generating generator sequence
-we can create sequence from generator by using for loop
-generator are better in performence than iterables
-generators take less time and memory
-when we want to perform task only once we can use generator
-when we want to perform task again & again we can use list.
-once we create generator and store it in variable then it iterate only one time
-you can iterate genrator again and again by genarating them
-generator comprehenssion is same as list but we use '()' paranthesis not use '[]'
"""
#iterable without for loop
# l=[1,2,3,4]
# n=iter(l)  '''iter() function create iter object of iterable'''
# print(next(n)) '''next() fuction point to element in iter function'''
# print(next(n))
# print(next(n))
# print(next(n))


#iterator with for loop--for loop already have iter() and next() function
# l=[1,2,3,4]
# for i in (map(lambda a:a**2,l)):
#     print(i)

#creating generator using 'yield' keyword
# def num(n):
#     for i in range(1,n+1):
#         yield i
# print(num(10))  ##it gives genrator object 
#for loop for creating generator sequence
# for n in num(10):  ##num() is function for generating sequence of 'n' nunbers
    # print(n)

#generator using variable
# def num(n):
#     for i in range(1,n+1):
#         yield i
# numbers=num(10)
# print(numbers)   ##return generator object
# for n in numbers:  ##printing sequence of generator
    # print(n)



#define generator function that can generate sequence of even number 
# def fun(n):
#     for i in range(1,n+1):
#         if i%2==0:
#             yield i
# for i in fun(100):
#     print(i,end=' ')


#generatr comprehenssion
# y= (i**2 for i in range(1,11))
# for num in y:
#     print(num)


#list vs generators
#using list --> take more time and memmory
# import time
# begin=time.time()
# l=[i**2 for i in range(1,1000000)]
# end=time.time()
# print(end-begin)

#using generators--> take less time and memory
# import time
# begin=time.time()
# g=(i**2 for i in range(1,1000000))
# end=time.time()
# print(end-begin)


#generator with lambda and yield
# def my_map(fun,l):
#     li=[]
#     for i in l:
#         li.append(fun(i))
#     yield li
# l=[12,4,5,6]
# var=my_map(lambda a: a**2,l)
# for i in var:  ##--> "var" is iterator
#     print(i)
