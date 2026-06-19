from database import *

create_table()

while True:
    print("\n===== Student Database Menu =====")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Get Student By ID")
    print("4. Update Marks")
    print("5. Delete Student")
    print("6. Students Above Marks")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter name: ")
        marks = int(input("Enter marks: "))
        insert_student(name, marks)
        print("Student added successfully!")

    elif choice == "2":
        students = get_all_students()

        if students:
            for student in students:
                print(student)
        else:
            print("No students found.")

    elif choice == "3":
        student_id = int(input("Enter student ID: "))
        student = get_student_by_id(student_id)

        if student:
            print(student)
        else:
            print("Student not found.")

    elif choice == "4":
        student_id = int(input("Enter student ID: "))
        new_marks = int(input("Enter new marks: "))
        update_marks(student_id, new_marks)
        print("Marks updated successfully!")

    elif choice == "5":
        student_id = int(input("Enter student ID: "))
        delete_student(student_id)
        print("Student deleted successfully!")

    elif choice == "6":
        threshold = int(input("Enter threshold marks: "))
        students = get_students_above(threshold)

        if students:
            for student in students:
                print(student)
        else:
            print("No students found.")

    elif choice == "7":
        print("Exiting...")
        break

    else:
        print("Invalid choice. Try again.")