l=[1234,'hello world',[1,2,4,5,6]]
print(l)


#  !Caution=> Lists are mutuable in python




# Operations we can perform on lists are:
# print(f'this will slice the list entire: {l[1:5]}')
# print(f'this will slice the list1: {str(l[0][1:3])}')
# print(f'this will slice the list2: {l[1][2:9]}')
# print(f'this will slice the list3: {l[2][2:6]}')


l2=[[1,2,34],[2,3,45],[4,3,2]]
firstCol=[row[0] for row in l2]
print(firstCol)