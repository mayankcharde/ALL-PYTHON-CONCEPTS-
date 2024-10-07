#  problem 1 
# n= 5
# for  i in range(1,11):
#   print(f"{n}X{i} = {n*i}")
  
#  problem 2
l = ["mayank" ,  "soham" ,"ansh", "rahul"]
for name in  l:
    if(name.startswith("m")):
        print(f"hello{name}")
        
#  problem 3      
# n =5
# i=1
# while(i<11):
#     print(f"{n} x {i} = {n*i}")
#     i+=1 
 
 
#  question4 
n= 5
for i in range (2,n):
    if(n%i) ==0:
        print("number is not prime")
        break
    else:
        print("number is prime!")
        
#    question5 
n = 5
i=0
sum =0
while(i<=n):
    sum +=1
    i +=1
print(sum)  

# question 6
#   FACTORIAL FINDING PROGRAM
n=5 
product =1
for i in range(1,n+1):
    product = product*i
    print(f"the factorial of{n} is {product}") 
    
    
# question 7
#   STAR PATTERN IN PYTHON 
'''
For n = 3
  *
 ***
*****

For n = 5
    *
   ***
  *****
 ********
**********

'''
n=5
for i in range(1,n+1):
    print(" " *(n-i) ,end="")
    print("*"*(2*i-1),end="")
    print(" ")

#  question 8 
n=3
for i in range (1, n+1):
    print("*" *i , end="")
    print("")
    
#  question 9 
#   DIFFICULT PROBLEM ON STAR PATTERN 
'''

***
* *       for n = 3
***


'''
n=5
for i in range(1 , n+1):
    if(i==1 or i==n):
        print("*"* n  , end="")
    else:
         print("*" , end="")
         print(" "*(n-2) , end="")
         print("*" , end="")
         print("")
         
#    question 10 
#  REVERSE ORDER OF TABLE PRINTING 
n=5
for i in range(1,11):
    print(f"{n} x {11-i} = {n*(11-i)}")  
 
