class Student:
    name = "not entered"
    age = "'not entered"
    marks = "not entered"
    
    def __init__(self , name , age , marks):
        self.name = "Your name:"+ name
        self.age = "Your Age :" + age
        self.marks ="Your Marks :" + marks
        
        
1 = Student(name= "HARSH" , age= "15" , marks="95")
2 = Student(name= "DEV" , age= "14" , marks="85")
n = 1
if n > 0 :
    b = print(f"{n}. student")
    n += 1
    print(f"{n.name}\n{n.age}\n{n.marks}")
else:
    pass

