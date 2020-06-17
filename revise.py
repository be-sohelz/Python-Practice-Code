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



for num in range(20):
    for i in range(num):
        print(num,end=' ')
    print('\n')









