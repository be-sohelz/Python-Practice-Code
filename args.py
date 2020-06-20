"""
-*args use to take multiple argument in funtion
-* help to take multiple value as argument
-acording to convention we use 'args' 
-our funtion take more input using *args 
"""

#normal function
# def add(a,b):
#     return a+b
# print(add(9,1))

#*args function--> take multiple argument as tuple
# def print_all(*args):
#     for i in args:
#         print(i)
# print(print_all(1,2,3,4,5,6,8,6))

#*args function for total  of number
# def total(*args):
#     total=0
#     for i in args:
#         total+=i
#     return total
# print(total(1,2,3,4))   """ take element as tuple """


#normal parameter with *args-->normal parameter(num) must be assingned before *args

# def mul(num,*args):
#     print(num)    """num = (9)"""
#     print(args)  """ args = (2,3,4)"""
#     mul=1
#     for i in args:
#         mul*=i
#     return mul
# print(mul(9,2,3,4))


# *args as argument 
# """ we can pass list,tuple as argument by unpacking with *args """
# def mul(*args):
#     mul=1
#     for i in args:
#         mul*=i
#     return mul
# l=[1,2,3,4]
# t=(1,2,3,4)
# print(mul(*l))  """ *l help to unpack list"""
# print(mul(*t))   """ *t help to unpack tuple"""


#W.F that can take normal parameter and *args
# def fun(num,*args):
#     l=[]
#     for i in args:
#         total=i**num
#         l.append(total)
#     if not args:
#         print("you din't enter any args")
#     return l
# ls=[1,2,3,4,5]
# print(fun(2,*ls))

