b='hello world and its going to end '
print(b)

#!caution:: Strins are immutable in python.

x=b[2:14]   #slicing of the string
print(x)

y=b[::4]    #used for slicing whole string and jumping it into 4
print(y)

z=b.split()    # will spilt the string and output will be in the array form
print(z)


q=b.split('o')   #spilitng will happen from o letter
print(q)


print(f' will capataalise whole string : {b.upper()}  \n will capatailise first letter :{b.capitalize()}')