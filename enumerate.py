#enumerate()  used to find position of element

#for without enumarate
# l=['name','age',24,5,2]
# pose=0
# for i in l:
#     print(f'pose is {pose}  :  {i}')
#     pose+=1


#for loop with enumerate() funtion
# l=['name','age',24,5,2]
# for i,j in enumerate(l):
#     print(f'pose {i} : {j}')


#W.F return posiotion of string/element in number
def find_pose(s,l):
    for pose,name in enumerate(l):
        if name==s:
            return pose
    return -1
l=['name','age',24,5,2]
print(find_pose('age',l))


