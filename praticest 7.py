#  problem 1
# def greatest (a,b,c):
#     if(a>b and a>c):
#         return a 
#     elif(b>a and b>c):
#         return b
#     elif(c>a and c>b):
#         return c
# a = 90
# b =70 
# c=20
# print(greatest(a,b,c)) 

# problem 2 
# #  tempertaure conversion problem
# def f_to_c(f):
#     return 5*(f-32)/9

# f =65
# c=f_to_c(f)
# print(f"{round (c,2)}^c") 
  
# question 3   
# print("a")
# print("b")
# print("c", end="")
# print("d", end="")  


# question 4 
# def sum(n):
#     if(n==1):
#         return 1
#     return sum(n-1) + n
# print(sum(4))

# #  question 5
# def pattern (n):
#     if(n==0):
#         return
#     print("*" * n)
#     pattern(n-1)
    
#     pattern(0)


#  question 6 
def inch_to_cms(inch):
    return inch *2.54

n=5
print(f"the corresponding cslue in cms is{inch_to_cms(n)}")


#  question  7
def rem (l, word):
    n=[]
    for item in l:
        if not (item == word):
            n.append(item.strip(word))
            return n 
        
l =["mayank" , "rohan ,33,3334,32111"]
print(rem(l , "mayank"))        


#  question  8
def multiply(n):
    for i in range (1,11):
        print(f"{n} x {i} = {n*i}")
multiply(9)



