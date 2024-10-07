#  question1 
name= "mayank"
marks =90
phone =552054522

s ="the name of the student is {} , his marks are {} and phone number is {}".format(name ,marks,phone)
print(s)

# question 2 
# table = [str(7*i) for i in range(1,11)]
# s= "\n".join(table)
# print(s)


# question 3 
def divisible(n):
    if(n%5==0):
        return True
    return False

a=[2,2,4,4,40,56,6,7,80,5,0]
f= list(filter(divisible , a))
print(f)

# question 4
from functools import reduce
l =[232,34,4,5,7,8,9,0]

def greater (a,b):
    if(a>b):
        return a 
    return b

print(reduce(greater,l))


