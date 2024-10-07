# #  question1 
# a1 = int(input("enter the number 1:"))
# a2 = int(input("enter the number 2:"))
# a3 = int(input("enter the number 3:"))
# a4 = int(input("enter the number 4:"))

# if(a1>a2 and a1>a3 and a1>a4):
#     print("greatest number is a1 " , a1)
# elif(a2>a1 and a2>a3 and a2>a4):
#     print("a2 is greater" , a2)
# elif(a3>a1 and a3>a2 and a3>a4):
#     print("a3 is greater" , a3)
# elif(a4>a1 and a4>a3 and a4>a2):
#     print("a4 is greater" , a4)
    
# question 2 
# marks1 = int(input("Enter Marks 1: "))
# marks2 = int(input("Enter Marks 2: "))
# marks3 = int(input("Enter Marks 3: "))
# total_percentage = (100*(marks1+marks2+marks3))/100

# if(total_percentage>=40 and marks1>=33 and marks2>=33 and marks3>=33):
#     print("youa re passed:" , total_percentage)
# else :
#     print("you are failed!")

# question 3 
# p1 = "Make a lot of money"
# p2 = "buy now"  
# p3 = "subscribe this"  
# p4 = "click this"
# message = input("enter your comment:")
# if((p1 in message)or (p2 in message)or (p3 in message)or (p4 in message)):
#     print("this comment a spam")
# else :
#     print("this nota a spam")

#  question4 
# username = input("enter username:")
# if(len(username)<10):
#     print("less than 10 characters ")
# else:
#     print("your username name contain more than 10 characters!")

#  question 5 
# l = ["Harry", "Rohan", "Shubham", "Divya"]

# name = input("Enter your name: ")

# if(name in l):
#     print("Your name is in the list")
# else:
#     print("Your name is not in the list")

#  question 6
# marks = int(input("enter your marks:"))
# if(marks <=100 and marks>=90):
#     grade ="e"
# elif (marks<90 and marks >=80):
#     grade ="a"
# elif (marks<80 and marks >=70):
#     grade ="b"
# elif (marks<70 and marks >=60):
#     grade ="c"
# elif (marks<60 and marks >=50):
#     grade ="d"
# elif (marks<50):
#     grade ="f"
#     print("your grade is :" , grade)

# question 7 
post = "Mayank"
if("mayank" in post.lower()):
    print("the post is talking about mayank")
else:
    print("this post is not talking about mayank")
