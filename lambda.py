"""
-lambda expression is anonymous function
-used for map, filter etc
-lambda function can be stored in variable
"""

#normal function for a+b
# def add(a,b):
#     return a+b
# print(add(10,20))

#lambda function for addtion is (lambda a,b: a+b)
# add=lambda a,b: a+b
# print(add(10,20))

#lambda function for divisible by 2 or not(True/False) is (lambda a: a%2==0)
# div=lambda a: a%2==0
# print(div(10))

#lambda for return last char of string is (lambda s: s[-1])
# last_char=lambda s: s[-1]
# print(last_char('sohel'))


#W.F return True if len(string)>5
#if else in normal function 
# def fun(s):
#     if len(s)>5:
#         return True
#     return False
# print(fun('sohel jagirdar'))


# if else in lambda for len(string)>5 print--> True
# fun=lambda s: True if len(s)>5 else False
# print(fun('sohel jagirdar'))

#len(string) >5 print -->True  lambdaa
# fun=lambda s: len(s)>5
# print(fun('jagirdar'))