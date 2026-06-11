def greet(name):
    print("Hello " + name + ", welcome to the grading system!")
def calculate_grade(marks):
    avg= sum(marks)/len(marks)
    if avg>90:
        return"A"
    elif avg>80:
        return"B"
    elif avg>70:
        return"c"
    elif avg>60:
        return"D"
    else:
        return'F'
           