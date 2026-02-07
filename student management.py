students = []
def calculate_grade(total):
    if total >= 270:
        return 'A'
    elif total >= 230:
        return 'B'
    elif total >= 200:
        return 'C'
    elif total >= 180:
        return 'D'
    else:
        return 'F'

def display_records():
    if not students:
        print("No student records found.")
    else:
        print("\nAll Student Records:")
        for student in students:
            print("ID:",student["ID"],"Name:", student["name"], " Marks:", student["marks"], " Grade:", student["grade"])


def filter_by_grade():
    grade = input("Enter grade to filter (A/B/C/D/F): ").upper()
    found = False
    for student in students:
        if student["grade"] == grade:
            print("ID:",student["ID"],"Name:", student["name"], "| Marks:", student["total"])
            found = True
    if not found:
        print("No students found with grade", grade)


def add_student():
    ID=int(input("enter the stydent id:"))
    name = input("Enter student name: ")
    marks1 = int(input("Enter student marks 1: "))
    marks2 = int(input("Enter student marks 2: "))
    marks3 = int(input("Enter student marks 3: "))
    total=marks1+marks2+marks3
    grade = calculate_grade(total)
    student = {"ID":ID, "name": name, "marks": total, "grade": grade}
    students.append(student)
    print("Student added successfully!")


def update_student_marks():
    id = int(input("Enter student id to update: "))
    for student in students:
        if student["ID"] == id :
            marks = int(input("Enter new marks: "))
            student["marks"] = marks
            student["grade"] = calculate_grade(marks)
            print("Marks updated successfully!")
            return
    print("Student not found.")


def delete_student():
    id = int(input("Enter student id to delete: "))
    for student in students:
        if student["ID"] == id:
            students.remove(student)
            print("Student deleted successfully!")
            return
    print("Student not found.")


while True:
    print("\n--- Student Management System ---")
    print("1. Display Records")
    print("2. Filter by Grade")
    print("3. Add Student")
    print("4. Update Student Marks")
    print("5. Delete Student")
    print("6. Exit")
    
    choice = input("Enter your Choice: ")

    if choice == '1':
        display_records()
    elif choice == '2':
        filter_by_grade()
    elif choice == '3':
        add_student()
    elif choice == '4':
        update_student_marks()
    elif choice == '5':
        delete_student()
    elif choice == '6':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number from 1 to 6.")