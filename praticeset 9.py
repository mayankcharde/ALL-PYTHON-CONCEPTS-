#  question 1 
class twodvector:
    def __init__(self ,i,j) -> None:
        self.i =i
        self.j =j
        
    def show(self):
            print(f"the vector is{self.i}i + {self.j}j")
            
            
class threedvector(twodvector):
    def __init__(self, i, j ,k) -> None:
        super().__init__(i, j)
        self.k =k     
        
    def show(Self):
        print(f"the vector is{Self.i}i + {Self.j}j + {Self.k}k")
        
        
a = twodvector(1,2)
a.show()
b = threedvector(4,5,6)
b.show()             

# question 2 
class animal:
    pass
class pets(animal):
    pass 
class dog(pets):
    @staticmethod
    def bark():
        print("bow bow")
     
d = dog()
d.bark()      
        
        
#  question 3 
class employee:
    salary =363
    increment =20
    
    @property
    def salaryafterincrement(self):
        return (self.salary + self.salary* (self.increment/100))
    
    @salaryafterincrement.setter
    def salaryafterincrement (self , salary):
        self.increment = ((salary/self.salary) -1)*100
        
e = employee()
e.salaryafterincrement =450
print(e.increment)


# question 4 
# class Complex:
#     def __init__(self, r, i):
#         self.r = r
#         self.i = i

#     def __add__(self, c2):
#         return Complex(self.r + c2.r, self.i + c2.i)
    
#     def __mul__(self, c2):
#         real_part = self.r * c2.r - self.i * c2.i
#         imag_part = self.r * c2.i + self.i * c2.r
#         return Complex(real_part, imag_part)
    
#     def __str__(self):
#         return f"{self.r} + {self.i}i"
        
    

# c1 = Complex(1, 2)
# c2 = Complex(3, 4)
# print(c1 + c2)
# print(c1*c2)


# question 5 
class vector:
    def __init__(self,x,y,z) -> None:
        self.x =x
        self.y=y
        self.z=z
        
    def __add__(self , other):
            result = vector(self.x + other.x , self.y + other.y , self.z +other.z)
            return result
        
    def __mul__(self , other):
            result = self.x * other.x + self.y * other.y +self.z * other.z
            return result
        
    def __str__(self):
            return f"vector({self.x} , {self.y} , {self.z})"
        
v1 = vector(1,2,3)
v2 = vector(4,5,6)
v3 = vector(7,8,9)

print(v1 + v2)
print(v1 * v2)
print(v1 + v3)
print(v1 * v3)        

# question 7 
class mayank:
    def __init__(self , i) -> None:
         self.i =i
         
         
    def __len__(self):
        return len(self.i)
    
m = mayank([1,2,3])
print(len(m))         
