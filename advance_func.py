#advanced max funtion

# l=['sohel jagirdar','s','name','age']

#max using func
# def func(a):
#     return len(a)
# print(min(l,key=func))
# print(max(l,key=func))


#min max using lambda function

# l=['sohel jagirdar','s','name','age']
# print(max(l,key=lambda a: len(a)))
# print(min(l,key=lambda a: len(a)))


#min max from list of dictonary
# l=[{'name':'sohel','score':50,'age':24},
# {'name':'fifa','score':24,'age':2},
# {'name':'babu','score':21,'age':4}
# ]
# print(max(l,key=lambda a: a.get('score'))['name'])
# print(max(l,key=lambda a: a.get('age'))['name'])
# print(min(l,key=lambda a: a.get('score'))['name'])
# print(min(l,key=lambda a: a.get('age'))['name'])


#reson behind printing name of scorer
# result=max(l,key=lambda a: a.get('score'))
# print(result)
# winner=result['name']
# print(winner)


#print min max scorer name from dictonary
# scores={
#     'sohel':{'score':70,'age':24},
#     'rifa':{'score':50,'age':5},
#     'rabi':{'score':52,'age':2}
# }
# print(min(scores,key=lambda i: scores[i]['score'] ))



#sort() & sorted() funtion
#we can sort list but not sort tuple,set
# fruites=['grapes','mango','banana','apple']
# print(sorted(fruites))
# print(fruites)
# fruites.sort()
# print(fruites)

# sorted() function with tuple
#sorted function return list of tuple not return tuple
# fruites=('grapes','mango','banana','apple')
# print(sorted(fruites))
# print(fruites)

# sorted() function with set
#sorted function return list of set not return set
# fruites={'grapes','mango','banana','apple'}
# print(sorted(fruites))
# print(fruites)


#sorted function on dictionary
# event=[{'name':'sohel','score':50,'price':24000},
# {'name':'fifa','score':24,'price':2100},
# {'name':'babu','score':21,'price':201}
# ]
# print(sorted(event,key = lambda d: d['price']))
#for reverse the dictionary price
# print(sorted(event,key = lambda d: d['price'], reverse=True))


#sort dictionary by score
# scores={
#     'sohel':{'score':70,'age':24},
#     'rifa':{'score':50,'age':5},
#     'rabi':{'score':52,'age':2}
# }
# print(sorted(scores,key=lambda i: scores[i]['score'],reverse=True ))

