from  typing import List
marks:list[float]=[]
for i in range(5):
    mark:float=float(input(f"Enter mark of subject {i+1}: ")
                )
    marks.append(mark)
average:float=sum(marks)/5
grade:str
if average>=90:
        grade="A"
elif average>=80:
        grade="B"
elif average>=70:
        grade="C"
elif average>=60:
        grade="D"
else :
        grade="F"
print("average marks:",average)
print("grade:",grade)                