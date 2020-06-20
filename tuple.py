"""
-tuple is data structure
-tuple are immutable
-tuple are faster than list
-no append,no pop, no remove,no insert in tuple
-we can do slicing like [:2] ,[-1] etc
-we can use function like len(),count(),index .etc 
"""

#basic tuple
# example=('sohel','rabi','rifa','raeah')
# print(example)
# print(len(example))
# print(example[:2])
# print(example[-1])

#creating tuple with range() function
# num=tuple(range(1,11))
# print(num)
# print(type(num))


#for loop in tuple
# example=('sohel','rabi','rifa','raeah')
# for i in example:
#     print(i, end=' ')

# while loop in tuple
# example=('sohel','rabi','rifa','raeah')
# i=0
# while i < len(example):
#     print(example[i],end=' ')
#     i+=1

#tuple with one element
# num=(1,)
# word=('sohel',)
# print(type(num))

#tuple without paranthesis
# numbers=1,2,3,4,5,6,7
# print(type(numbers))

#tuple unpacking (method 1)
# song1, song2, song3=('lost my way','bermuda','worrior')
# print(song1,song2,song3)

#tuple unpacking (method 2)
# songs=('lost my way','bermuda','worrior')
# s1,s2,s3=songs
# print(s1,s2,s3)

#list inside tuple
# example=('sohel',[1,2,3,4,5],'rabi','rifa','raeah')
# example[1].insert(5,'six')
# example[1].append(7)
# print(example)

#list inside tuple using for loop
# example=('sohel','rabi',['zero'],'rifa','raeah')
# for i in range(10):
#     example[2].append(i)
# print(example)

#list in tuple using  range() & append()
# numbers=list(range(1,10))
# example=('sohel','rabi',['zero'],'rifa','raeah')
# example[2].append(numbers)
# print(example)

#list inside tuple using pop and append with for loop
# example=('sohel','rabi',['zero',1,2,3,4,5],'rifa','raeah')
# new=[]
# for i in range(len(example[2])):
#     popped=example[2].pop()
#     new.append(popped)
# print(new)


#function returning two values
"""
whenever we take return two values from function, its return tuple of those two value.
we can store them into two diff. variable and make them seprete.
 """
 #Eg.
# def two_value(int1,int2):
#     add=int1+int2
#     mul=int1*int2
#     return add , mul
# print(two_value(2,3)) """it give tuple as output :-> (5, 6) """
# add,mul=two_value(2,3)  """ it give seprete output for add and mul : 5  6"""
# print(add)
# print(mul) 


#creating tuple,list,str with range() function

#tuple:-->

# num=tuple(range(1,11))
# print(num)
# print(type(num))

#lists:-->
# num_list=list(range(1,10))
# print(num_list)
# print(type(num_list))

#changing tuple to list
# numbers=(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
# numbers_list=list(numbers)
# print(numbers_list)
# print(type(numbers_list))

#changing list to tuple
# number=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# number_tuple=tuple(number)
# print(number_tuple)
# print(type(number_tuple))

#changing list to string 
# num=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# string=str(num)
# print(string)
# print(type(string))

#changing tuple to string 
# num=(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
# string=str(num)
# print(string)
# print(type(string))

