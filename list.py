"""-list is an type of datatype in python
   -it can store all type of data like int,float,string,boolean etc
   -list support indexing same like string
   -you can chage index value by assigning new value
   -mostly used to store and retrieve data
 """
#List Basic Operation
# number=[0,1,2,3,'four','five','six',7.0,8.0,9.0,None,True,False]
# print(number)
# print(type(number))
# print(number[-1])
# print(number[::-1])
# number[1]='one'
# print(number)
# number[:4]=['zero','one','two','three']
# print(number)


#list in tuple using  range() & append()
# numbers=list(range(1,10))
# example=('sohel','rabi',['zero'],'rifa','raeah')
# example[2].append(numbers)
# print(example)


#add Data to list (append method)
# fruits=[]
# fruits.append('banana')
# fruits.append('oranges')
# fruits.append('apple')
# fruits.append('mango')
# print(fruits)


#check list is empty or not method 1
# l=[]
# if not l:
#     print('empty')
# else:
#     print('not empty')

#check list is empty or not method 2
# l=[]
# if len(l)>0:
#     print('not empty')
# else:
#     print('empty')

#check list is empty or not method 3
# l=[]
# if l:
#     print('not empty')
# else:
#     print('empty')


#more method to add data in list like insert(),extend(),l1 + l2, append()

#extend method  -> add all elements from list
# even=[0,2,4,6,8]
# odd=[1,3,5,7,9]
# even.extend(odd)
# print(even)
# print(odd)

#insert method -> add element at position
# even=[0,2,4,6,8]
# even.insert(1,1)
# print(even)

#addition method -> add two lists
# even=[0,2,4,6,8]
# odd=[1,3,5,7,9]
# even_odd= even + odd
# print(even_odd)

#append method -> it add list inside list
# even=[0,2,4,6,8]
# odd=[1,3,5,7,9]
# even.append(odd)
# print(even)


#delete method for list like pop,remove,del

#pop() method -> pop from last element or from given index value
# fruites=['banana','apple','mango','grapes']
# popped_item1=fruites.pop()
# popped_item2=fruites.pop(0)
# print(popped_item1, popped_item2)

#remove() method -> remove given element in list from anywere else only first element
# fruites=['banana','apple','mango','grapes']
# fruites.remove('banana')
# print(fruites)

#del -> delete element from list using index value
# fruites=['banana','apple','mango','grapes']
# del [fruites[1]]
# print(fruites)


#in keyword -> check velue is present or not
# name=['sohel','rabi','rifa','naz']
# if 'sohel' in name:
#     print('yes')
# else:
#     print('no')


#some more method for list count(),sort(),sorted(),clear(),copy()

#count method -> count given element
# num=[5,8,3,9,4,8,6,5,2,1]
# count=num.count(8)
# print(count)

#sort() method -> sort main list in increasing order
# num=[5,8,3,9,4,8,6,5,2,1]
# num.sort()
# print(num)

#sorted method -> print sorted number without changing main list
# num=[5,8,3,9,4,8,6,5,2,1]
# print(sorted(num))
# print(num)

#copy() method -> copy all element from list 
# num=[5,8,3,9,4,8,6,5,2,1]
# num_copy=num.copy()
# print(num)
# print(num_copy)

#clear() -> clear all the elements from list or make list empty
# num=[5,8,3,9,4,8,6,5,2,1]
# num.clear()
# print(num)


#split and join method

#split method -> strings to list element
# user_info='sohel jagirdar'.split()
# print(user_info)

#string assign to variable
# name,age='sohel,24'.split(',')
# print(name)
# print(age)

#join(method)--> return list element to strings
# user=['sohel','jagirdar']
# print(','.join(user))
# print(user)


#for loop and while loop for list

#for loop
# fruites=['banana','apple','mango','grapes']
# for fruite in fruites:
#     print(fruite)

#while loop 
# fruites=['banana','apple','mango','grapes']
# i=0
# while i<len(fruites):
#     print(fruites[i])
#     i+=1



#list inside list (2D list)
# matrix=[[1,2,3],[4,5,6],[7,8,9]]
# print(matrix[1])
# for i in matrix:
#     for j in i:
#         print(j,end=' ')

#accessing list inside list element i.e (5 & 7) from list 
# matrix=[[1,2,3],[4,5,6],[7,8,9]]
# print(matrix[1][1])
# print(matrix[2][0])

#printing negative list function
# num=[5,8,3,9,4,8,6,5,2,1]
# def neg_list(l):
#     n_list=[]
#     for i in l:
#         n_list.append(-i)
#     return n_list
# print(neg_list(num))




#exersise / practice

#function take list as input and return square of list
# number=list(range(1,10))
# def square(l):
#     sqr=[]
#     for i in l:
#         sqr.append(i*i)
#     return sqr
# print(square(number))

#write a function wich return reverce of string
# number=list(range(1,10))
# def reverce(l):
#     rev=[]
#     rev.append(l[::-1])
#     return rev
# print(reverce(number))

#reverse using indexing [::-1]
# number=list(range(1,10))
# def rev(l):
#     return l[::-1]
# print(rev(number))


#reverse list by using pop() and append()
# number=list(range(1,10))
# def reverce(l):
#     reverced=[]
#     for i in range(len(l)):
#         popped=l.pop()
#         reverced.append(popped)
#     return reverced
# print(reverce(number))

#reverse using reverse() method
# number=list(range(1,10))
# number.reverse()
# print(number)

#write function to reverse string in list
# words=['sohel','rabi','rifa','raeah']
# def rev_string(l):
#     new_rev=[]
#     for i in l:
#         rev=i[::-1]
#         new_rev.append(rev)
#     return new_rev
# print(rev_string(words))

#W.F to rev string
# words=['sohel','rabi','rifa','raeah']
# def rev(l):
#     string=[]
#     for i in l:
#         string.append(i[::-1])
#     return string
# print(rev(words))

#list return list with even_odd elements (method 1)
# number=list(range(1,10))
# def even_odd(l):
#     even_odd=[]
#     even=[]
#     odd=[]
#     for i in l:
#         if i%2==0:
#             even.append(i)
#         else:
#             odd.append(i)
#     even_odd.append(even)
#     even_odd.append(odd)
#     return even_odd
# print(even_odd(number))

##list return list with even_odd elements (method 2)
# number=list(range(1,10))
# def even_odd(l):
#     even=[]
#     odd=[]
#     for i in l:
#         if i%2==0:
#             even.append(i)
#         else:
#             odd.append(i)
#     even_odd=[even,odd]
#     return even_odd
# print(even_odd(number))

#W.F take 2 list as input and return common element (method 1)
# a=[1,2,4,6,8,9,7]
# b=[1,4,8,4,99,66]
# def common(l1,l2):
#     common=[]
#     for i in l1:
#         for j in l2:
#             if i==j:
#                 common.append(i)
#     return common
# print(common(a,b))

#W.F take 2 list as input and return common element (method 2)
# a=[1,2,4,6,8,9,7]
# b=[1,4,8,4,99,66]
# def common(l1,l2):
#     common=[]
#     for i in l1:
#         if i in l2:
#             common.append(i)
#     return common
# print(common(a,b))

 
#min() & max() function

#W.F to find diffrence (method 1)
# number=[2,60,25,40]
# def diffrence(l):
#     return max(l)-min(l)
# print(diffrence(number))

#W.F to find diffrence (method 2) output is in list
# number=[2,60,25,40]
# def diffrence(l):
#     diff=[]
#     a=min(l)
#     b=max(l)
#     c=b-a
#     diff.append(c)
#     return diff
# print(diffrence(number))

#count list inside list
# lists=[1,2,3,[4,5,6],7,[8,9],10,[11,12],13]
# def lists_count(l):
#     counts=0
#     for i in l:
#         if type(i)==list:
#             counts+=1
#     return counts
# print(lists_count(lists))
    