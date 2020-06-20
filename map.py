""" 
-map() funtion iterate list,tuple
-map function is iterator 
-map function use with lambda expression
-we can iterate filter() and map() object only once
-we can iterate list,tuple,string multiple time
"""
#map function help to iterate list/tuple by using other function

# num=[1,2,3,4]
# def square(a):
#     return a**2
# print(list(map(square, num)))

#map function return reverse of string
# s=['sohel','usman']
# def rev(s):
#     return s[::-1]
# print(list(map(rev,s)))


#map() with lambda [return square of number]
# number=[1,2,3,4,5]
# print(list(map(lambda a: a**2,number)))

#square using list comprehenssion
# l=[1,2,3,4,5]
# s=[i**2 for i in l]
# print(s)


#without comprehension and without map() function
# def sqr(a):
#     return a**2
# number=[1,2,3,4,5]
# l=[]
# for i in number:
#     l.append(sqr(i))
# print(l)

#map() for len(string)
# name=['soed','ddsff','sdfsdfsdf']
# print(list(map(lambda a: len(a),name)))

#list return True/False number is even or odd with True/False list
# l=[1,2,3,4,5,6,7,8,9]
# print(list(map(lambda a: a%2==0,l)))



""" 
-filter() funtion return value if True
-filter function is iterator 
-filter function use with lambda expression
-we can iterate filter and map object only once
-we can iterate list,tuple,string multiple time
"""
# l=[1,2,3,4,5,6,7,8,9]
# even=filter(lambda a: a%2==0,l)
# print(list(even))


#iterating filter object
# l=[1,2,3,4,5,6,7,8,9]
# even=filter(lambda a: a%2==0,l)
# for i in even:
#     print(i)
# for i in even: ##""" <-- we cant iterate map() function more than one"""
#     print(i)





"""
-zip() function used to combine value from two diff list/dictionary
-zip() can use to create dictionary if tuple contain only two values
-if list/tuple have diff value then zipping stop after smallest value
-we can convert zip() to list,tuple and dictionary
-using *l operator we can unpack list
"""

#zip() function 
# user=['user1','user2','user3','user4']
# name=['sohel','rabi','rifa','raeah']
# print(list(zip(user,name)))

#zip() to dictionary
# user=['user1','user2','user3','user4']
# name=['sohel','rabi','rifa','raeah']
# new_dict=dict(zip(user,name))
# print(new_dict)

#normal list of tuple to dictionary
# t=[(1,'a'),(2,'b'),(3,'c')]
# t_dict=dict(t)
# print(t_dict)


#convert list of tuple to list using zip() function
# l=[(1,2,),(3,4),(5,6),(7,8)]
# l1,l2=list(zip(*l))
# print(list(l1))
# print(list(l2))

#for finding greater number from list of tuple
# l=[(1,2,),(3,4),(5,6),(7,8)]
# l1,l2=list(zip(*l))
# max_list=[]
# for pair in zip(l1,l2):
#     max_list.append(max(pair))
# print(max_list)


"""
-all() function check that all elements are same or not
-any() function check that a single element is same or not
"""
#all() function
# l1=[1, 3, 5, 7]
# l2=[2, 4, 6, 8]
# new_l=[]
# for i in l2:
#     if i%2==0:
#         new_l.append(True)
# print(new_l)

#all()--> True if all elment is true
# l2=[2, 4, 6, 8]
# l=[]
# for i in l2:
#     if i%2==0:
#         l.append(True)
# print(all(l))


#any()--> True if an single element is true
# l2=[2, 5, 9, 7 ]
# l=[]
# for i in l2:
#     if i%2==0:
#         l.append(True)
# print(any(l))

#check all() function--> check all are True
# print(all([True, True, True]))

#check any() function an element is True
# print(any([True, False, True, True, True]))



#all() function for check input is int and float are given else return wrong input
 
# def add_sum(*args):
#     if all([(type(i) == int or type(i) == float) for i in args]):
#         sum=0
#         for num in args:
#             sum+=num
#         return sum
#     else:
#         return 'wrong input'
# print(add_sum(1,2,3,4,5.5,25.2,'sohel'))



        















