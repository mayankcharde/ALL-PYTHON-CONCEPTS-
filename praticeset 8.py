from random import randint
# # program 1
# class program:
#     company = "microsoft"
#     def __init__(self , name , salary,pin) -> None:
#         self.name = name 
#         self.salary = salary
#         self.pin = pin
        
#         p= program("mayank" , 1200000 , 537392)
#         print(p.name ,p.salary,p.company)
#         r= program("rohan" , 12992, 734747)
#         print(r.name , r.pin , r.company) 
        
# question 2 
# class calculator:
#      def __init__(self ,n) -> None:
#           self.n =n
          
#      def square (self):
#          print(f"the square is{self.n*self.n}")
         
#      def cube(self):
#          print(f"the cube is {self.n*self.n*self.n}")
         
#      def squareroot(self):
#          print(f"the squareroot is{self.n**1/2}") 
         
# a= calculator(4)
# a.square()
# a.cube()
# a.squareroot()        

# question 3 
# class demo:
#     a=4
    
# o= demo()
# print(o.a)
# o.a =0
# print(o.a)
# print(demo.a)

# question 4 
class train:
    def __init__(self , trainno) -> None:
        self.trainno = trainno
        
    def book(self , fro , to):
        print(f"the tickit is booked in train no:{self.trainno} from {fro} to {to}")
        
    def getstatus(self):
        print(f" the train no:{self.trainno} is running on time")
            
    def getfare(self , fro , to):
        print(f"tickit fare in train no:{self.trainno}  from {fro} to {to} is {randint(222 , 555)}")
        
t = train(123454)
t.book("nagpur" , "delhi")
t.getstatus()
t.getfare("nagpur" , "delhi")        
                
                
            
