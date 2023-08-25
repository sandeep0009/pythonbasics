

x=15

if (x<5):
    print('hi welcome kid')
else:
    print('hi man')



#if-elif-else:
y=22
if (y<18):
    print('not eligible for voting')
elif(y>18 and y<21):
    print('eligible for voting')
else:
    print('eligible for voting and participating in elections')




#for loop:
for i in range(1,11):
    print(f' 2 X {i} = {2*i}')





#while loop :
i=5
while(i!=0):
    print(i)
    i=i-1




#list compression:
x=[1,2,3,4,5]
out=[num**2 for num in x]
print(out)