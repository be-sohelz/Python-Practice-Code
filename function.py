#add two number
# def add(a,b):
#     return a+b
# print(add(10,20))


# #add two num with input
# def add_num(num1,num2):
#     return num1+num2
# a=int(input('enter number 1 : '))
# b=int(input('enter number 2 : '))
# print(add_num(a,b),'is addition of number ')


#add two num with input
# def add_string(s1,s2):
#     return s1+s2
# a=input('enter string 1 : ')
# b=input('enter string 2 : ')
# print(add_string(a,b),' is addition of string ')

#function return last charector
# def last_char(a):
#     return a[-1]
# print(last_char('sohel'))


#odd even number
# def odd_even(n):
#     if n%2==0:
#         return 'even number'
#     else:
#         return 'odd number'
# print(odd_even(21))


# def odd_even(n):
#     if n%2==0:
#         return 'even number'
#     return 'odd number'
# print(odd_even(20))


# pythonic way True Or False
# def is_even(n):
#     return n%2==0
# print(is_even(20))


# fuction for find greater number
# def greater(a,b):
#     if a>b:
#         return 'a is greater '
#     return 'b is greater '
# a=int(input("enter num a "))
# b=int(input("enter num b "))
# print(greater(a,b))


# greatest from a,b,c
# def greatest(a,b,c):
#     if a>b and a>c:
#         return a
#     elif b>a and b>c:
#         return b
#     else:
#         return c
# a=int(input("enter num a "))
# b=int(input("enter num b "))
# c=int(input("enter num c "))
# print(greatest(a,b,c))


# function inside function
# def great(a,b):
#     if a>b:
#         return a
#     return b
# a=int(input("enter num a"))
# b=int(input("enter num b "))
# c=int(input("enter num c "))
# bigger=great(a,b)
# def greater(bigger,c):
#     if bigger>c:
#         return bigger
#     return c
# print(greater(bigger,c))


# check string is polindrome or not
# def is_polindrome(a):
#     if a==a[::-1]:
#         return True
#     return False
# a=input('enter a string : ')
# print(is_polindrome(a))


# pythonic way for is_polindrome or not
# def is_polindrom(s):
#     return s==s[::-1]
# s=input("enter a string : ")
# print(is_polindrom(s))


# Fibonacci series
# def fibonacci(n):
#     a=0
#     b=1
#     if n==1:
#         print(a)
#     elif n==2:
#         print(a, b)
#     else:
#         print(a, b, end=" ")
#         for i in range(n-2):
#             c=a+b
#             a=b
#             b=c
#             print(c,end=" ")
# print(fibonacci(15))


# Default parameter
# def user_info(name,last_name,age=24):
#     print(f'name is : {name} \nlast name is : {last_name} \nage is {age}')
# user_info('sohel','jagirdar')


# #scope of variables
# x=7 ##globle variable
# def fun():
#     global x
#     x=5   ##local Variable
#     return x
# print(x)
# print(fun()) ##5
# print(x)



#fibonacci series practice
# def fib(n):
#     a=0
#     b=1
#     if n==1:
#         print(a)
#     elif n==2:
#         print(a,b)
#     else:
#         print(a,b,end=' ')
#         for i in range(n-2):
#             c=a+b
#             a=b
#             b=c
#             print(c,end=' ')
# print(fib(10))