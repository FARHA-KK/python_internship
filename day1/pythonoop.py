class student:
    def __init__(self,id,name,marks):
        self.id=id
        self.name=name
        self.marks=marks
    
    def grade(self):
               if self.marks>=90:
                  return"A"
               elif self.marks>=80:
                    return"B"
               elif self.marks>=70:
                    return"C"  
               elif self.marks>=60:
                    return"D"
               else:
                    return"F"
    def display(self):
        print("ID:",self.id)
        print("Name:",self.name)
        print("marks:",self.marks)
        print("grade:",self.grade())
s1=student(1,"Anu",95)
s2=student(2,"Adhi",88)
s3=student(3,"Nidhu",55)
students=[s1,s2,s3]
for student in students:
    student.display()
    

              