"""
-Dictinary is unordered collection of data stored in 'key','value' pair.
-dictionary can store anything : number,string,list,tuple,dictionary .etc
-dictionary can store very complex data.
"""

#(method 1 )dictionaries
# dic1={
#     'name':'sohel',
#     'age':24,
# }
# print(dic1)
# print(type(dic1))

#(method 2 )dictionaries using dict()
# user=dict(name='sohel',age=24)
# user2=dict(name='sohel',age=24)
# print(user2)
# print(user)

#how to access dictionary value
# user1={
#     'name':'sohel',
#     'age':24,
#     'fav_movies':['john wick','arjun reddy','geetha govindam'],
#     'fav_song':['bermuda','waka waka','worrior']
# }
# print(user1['fav_song'])
# print(user1['fav_movies'])

#how to add data to empty dictionary
# users_info={}
# users_info['name']='sohel'
# users_info['age']=24
# users_info['hight']=5.10
# print(users_info['age'])


#'in' keyword in dictionary
# users_info={
#     'name':'sohel',
#     'age':24,
#     'fav_movies':['john wick','arjun reddy','geetha govindam'],
#     'fav_song':['bermuda','waka waka','worrior']
# }

#in keyword  --> check for "key" (by default)
# if 'names' in users_info:
#     print('yes')
# else:
#     print('no')

# in keyword  --> check for "key"
# if 'names' in users_info.keys():
#     print('yes')
# else:
#     print('no')

#in keyword  --> check for "values"
# if 'sohel' in users_info.values():
#     print('yes')
# else:
#     print('no')





#looping in dictionary
# users_info={
#     'name':'sohel',
#     'age':24,
#     'fav_movies':['john wick','arjun reddy','geetha govindam'],
#     'fav_song':['bermuda','waka waka','worrior']
# }

#for loop --> return keys
# for i in users_info:
#     print(i)

#.keys() method --> return tuple of keys
# keys=users_info.keys()
# print(keys)

#for loop with .keys() method --> return keys
# for i in users_info.keys():
#     print(i)

#for loop with values() method --> return values
# for i in users_info.values():
#     print(i)

#.values() method --> return tuple of values 
# values=users_info.values()
# print(values)

#for loop for values ---> return values
# for i in users_info:
#     print(users_info[i])


#.item() method
#.items() method --> return tuple of key and value pair
# item=users_info.items()
# print(item)
# print(type(item))


#for loop with .item() method --> "i" return 'key' & "j" return 'values'
# for i,j in users_info.items():
#     print(f'key is "{i}" : value is "{j}"') 



#adding data to dictionary
# cricketer={
#     'dhoni':['csk','ipl','india'],
#     'rohit':['mi','ipl','india'],
#     'kohli':['rcb','ipl','india']
# }

#adding data to cricketer dictionary
# cricketer['raina']=['csk','ipl','india']
# cricketer['pandya']=['mi','ipl','india']

#pop()--> pop data from dictionary(|you must pass key in pop()|.its not like list.pop()
# poppped_1=cricketer.pop('dhoni')
# poppped_2=cricketer.pop('pandya')
# print(poppped_1,poppped_2)

#popitem()--> do not pass any value in popitem,it pop random item from dictionary
# popped_item=cricketer.popitem()
# print(popped_item)


#update method

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
# print(user)
# print(user1)

# update method
# user.update(user1)
# print(user)

#if dictionary have same value last value override same value
# user={
#     'name':'sohel',
#     'age':24,
#     'age':21
# }
# print(user.get('age'))



#creating dictionary by fromkeys() method
#it help to create dictionary with custom value

#fromkeys() method
# user=dict.fromkeys(['name','age','hight'],'unknown')
# print(user)

#multiple values --> you can use list,tuple.etc
# user=dict.fromkeys(['name','age','hight'],['unknown','unknown','unknown'])
# print(user)

#range function in .fromkeys() method
# number=dict.fromkeys(range(1,11),'unknown')
# print(number)

#get() method --> get kry and return value or return None if value not present
# names={
#     'name1':'sohel',
#     'name2':'rabi',
#     'name3':'rifa',
#     'name4':'raeah',
# }

#.get() method
# name=names.get('name1')
# print(name)

#.get() with if_else
# if names.get('name1'):
#     print('present')
# else:
#     print('not present')

#more about .get() method
#you can set 'None' With your defoult massage like 'key not found'
# print(names.get('name8','key not found'))


#.copy() and .clear() method

# names={
#     'name1':'sohel',
#     'name2':'rabi',
#     'name3':'rifa',
#     'name4':'raeah',
# }

#.copy() --> help to copy dicionary 
# names_copy=names.copy()
# print(names_copy)


#clear()--> clear our dictionary
# names.clear()
# print(names)

#W.F take number as input  and return cube of number
# def cub_finder(n):
#     cube={}
#     for i in range(n+1):
#         cube[i]=i**3
#     return cube
# number=int(input('enter no for cube'))
# print(cub_finder(number))


#W.F that can count words string and store in dictonary
# def word_counter(s):
#     counted={}
#     for i in s:
#         counted[i]=s.count(i)
#     return counted
# print(word_counter('ssohels'))


# W.A.P to enter value from user
# user={}
# name=input('enter name')
# age=int(input(' enter name'))
# fav_movies=input('enter fav movies sep by "," ').split(",")
# fav_song=input("enter fav song sep by ',' ").split(",")
# user['name']=name
# user['age']=age
# user['fav_movies']=fav_movies
# user['fav_song']=fav_song
# print(user)