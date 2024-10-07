# import random
#  problem 1 
# f = open("poem.txt")
# content =f.read()
# if("twinkle" in content):
#     print("the word twinkle is in content")
# else:
#     print("the word twinkle not present in content")
    
#     f.close()
    
#  problem 2 

def generateTable(n):
    table = ""
    for i in range(1, 11):
        table += f"{n} X {i} = {n*i}\n"
    
    with open(f"tables.txt", "w") as f:
        f.write(table)
        
for i in range(1,11):
    generateTable(5)
    
#  question 3 
word = "donkey"

with  open("file.txt" , "r") as f :
    content =f.read()
    
contentnew = content.replace(word , "####")
with open("file.txt" , "w") as f :
    f.write(contentnew)
    
        
    
# question 4
words = ["mayank" , "hello" , "hey"]
with open("myfile.txt" , "r") as f :
    content = f.read()
    
    for word in words:
        content = content.replace(word , "$" )
        
        with open("myfile.txt" ,  "w") as f:
            f.write(content)
  
    
# question 5
with open ("log.txt") as f:
    content = f.read()
    
    if("python" in content):
        print("yes it is")
    else :
        print("it is not present") 
        
        
# problem  6
with open("log.txt") as f:
    lines = f.readlines()
    
    lineno =1
    for line in lines:
        if("python" in line):
            print(f"yes python is present . line no:{lineno}")
            break
        lineno+=1
        
    else :
        print("no it is not present")
        
        
# question 7
# FOR COPYING CONTENT FROM ONE FILE TO ANOTHER 
with open ("this.txt") as f :
    content =f .read()
    
    with open("this_copy.txt" , "w") as f :
        f.write(content) 
        
        
# question  8
with open ("this.txt") as f :
    content =f.read()
    
    with open ("this_copy.txt") as f :
        content2 = f.read()
        
    if(content == content2):
        print("yes these files are identical")
        
    else :
        print("not identical")    
        
        
# question  9
#  FOR MAKING A FILE EMPTY
# with open("this_copy.txt" ,"w") as f:
#     f.write("")


# question 10
with open ("old.txt") as f :
    content = f.read()
    
    with open("renamed_by_python.txt" ,'w') as f :
        f.write(content)
