import util
name=input("Enter your name: ")


marks=[]
for i in range(5):
    mark=float(input(f"enter mark of subject{i+1}:"))
    marks.append(mark)
    
util.greet(name) 
print("your grade is:",util.calculate_grade(marks))