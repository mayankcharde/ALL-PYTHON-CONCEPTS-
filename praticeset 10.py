#  question 1 
try:
    with open("1.txt" , "r") as f :
        print(f.read())
except Exception as e :
    print(e)
    
try:
    with open ("2.txt" , "r") as f :
        print(f.read())
except Exception as e :
    print(e)
    
try:
    with open ("3.txt" ,'r') as f :
        print(f.read())
except Exception as e:
    print(e)
    
print("thenkyou")     


#  QUESTION 2 
L =[1,2,3,4,4,6,7,78,9,0]

for index, item in enumerate(L):
    if index == 2 or index == 4 or index == 6:
        print (f"{item} on index {index}")


# QUESTION 3         
n=45

table =[n*i for i in range (1,11)]
print(table)  


#  QUESTION 4 
try:
    a=22
    # b=0
    b=2
    print(a/b)
except Exception as e :
    print("infinite")
    
    
    
#  QUESTION 5
n=5
table = [n*i for i in range(1,11)]
with open ("mayanktable.txt" , "a") as f:  # FOR ADDING WE USE APPEND 
    f.write(f"table of{n}: {table} \n") 
