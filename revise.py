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

fru=[]
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