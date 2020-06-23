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