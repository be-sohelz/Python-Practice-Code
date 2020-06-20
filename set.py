"""
-set is unordered collection of data
-set used to  remove redundancy / repeatation
-some operation on set like : add(),remove(),dicscard(),copy(),clear()
-we can change list to set and also set to list
-set can't be modified like list
"""

#create set 
# number={1,2,2,3,4,5,5,6,6}
# print(number)

#set can store
# set_demo={1,1.1,2,3,'four','five',False}
# print(set_demo)

#remove redundancy of list using set{}
# number=[1,1,2,2,3,4,5,5,6,8,9,8,9]
# s=set(number)
# n=list(s)
# print(n)

#adding element in set using add()
# set_demo={1,1.1,2,3,'four','five',False}
# set_demo.add('nine')
# set_demo.add('ten')
# print(set_demo)

#removing element from set using remove()
# set_demo={1,1.1,2,3,'four','five',False}
# set_demo.remove(1)
# set_demo.remove('five')
# print(set_demo)

#remove element using discard() method --> remove element else do nothing.
# set_demo={1,1.1,2,3,'four','five',False}
# set_demo.discard(2)
# set_demo.discard('five')
# set_demo.discard('obama')
# set_demo.discard(1111)
# print(set_demo)

#copy() & clear() method

#copy() method
# set_demo={1,1.1,2,3,'four','five',False}
# set_copy=set_demo.copy()
# print(set_copy)

#clear() method
# set_demo={1,1.1,2,3,'four','five',False}
# set_demo.clear()
# print(set_demo)

#in keyword in python
# s={1,1.1,2,3,'four','five',False}
# if 'five' in s:
#     print('present')
# else:
#     print('not present')

#for loop in set
# s={1,1.1,2,3,'four','five',False}
# for i in s:
#     print(i)

#UNION and INTERSECTION in set

#Union ( | ) --> diffrent element from two set or it eliminate redundent value
# a={1,2,3,4}
# b={3,4,5,6}
# union= a | b
# print(union)

#INTERSECTION ( & ) --> produce common value from two sets
# a={1,2,3,4}
# b={3,4,5,6}
# intersection= a & b
# print(intersection)
