def arrayseqeuence(num):
    for i in range(len(num)-2):
        if num[i]==1 and num[i+1]==2 and num[i+2]==3:
            return True
    
    return False


x=[1,2,3,4,5,1,2,3,55,6,3]          #return true if sequence of 1,2,3 exists
print(arrayseqeuence(x))


def stringBits(mystr):
    result=''
    for i in range(len(mystr)):
        if i%2==0:
            result=result+mystr[i]
    
    return result

mystr='helooo'
print(stringBits(mystr)) 

def doublestring(mystr):
    result=''
    for char in myst:
        result+=char*2

    return result

myst='hello'
print(doublestring(myst))