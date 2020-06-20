"""
-kwargs is keyword argument(**kwargs)
-kwargs is dictionary datatype
-**kwargs used to unpack dictionary
"""

#**kwargs --> printing kwargs

# def fun(**kwargs):
#     print(kwargs)
# fun(name='sohel',age=24)


#unpacking dictionary using kwargs
# def fun(**kwargs):
#     for k,v in kwargs.items():
#         print(f'{k} : {v}')
# d={'name':'sohel','age':24,}
# fun(**d)

#normal parameter with **kwargs
# def fun(num,**kwargs):
#     for k,v in kwargs.items():
#         print(f'{k} : {v}')
# d={'name':'sohel','age':24,}
# fun(1,**d)


#sequence of function parameter
#PADK (parameter,*args,defoult parameter,**kwargs)
# def fun(name,*args,last_name='jr',**kwargs):
#     print(name)
#     print(args)
#     print(last_name)
#     print(kwargs)
# fun('sohel', 1,2,3, a=1,b=2)


# #
# def fun(l,**kwargs):
#     if kwargs.get('reverse')==True:
#         for i in l:
#             return i[::-1].title()
#     else:
#         for i in l:
#             return i.title()
# name=['sohel','ahe']
# print(fun(name,reverse=True))
        
    