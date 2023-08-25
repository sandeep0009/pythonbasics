def add(num1,num2):
    if(type(num1)==type(num2)==type(10)):
        return num1+num2
    else:
        return ("sorry need of integers")


a=add(20,4)
print(a)

b=add('12',2)
print(b)


#filter function:

list1=[1,2,4,4,5,6,7,8,9,10]

def evenBool(num):
    return num%2==0

even=filter(evenBool,list1)
print(list(even))


#lamda functions:

odd=filter(lambda num:num%2!=0,list1)
print(list(odd))