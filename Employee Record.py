#Create a Python program to manage employee records
employees=[]

def add_employee():
    ID=int(input("enter the employee ID:"))
    name=input("entet the employee name:")
    department=input("enter the employee Department:")
    salary=int(input("enter the employee Salary:"))
    employee={'ID':ID, 'name':name,'department':department,'salary':salary}
    employees.append(employee)

def display():
    if not employees:
        print("No Employee records found!!")
    else:
        print("\nEmployee records-> ")   
        for employee in employees:
            print("ID:",employee["ID"],'NAME',employee['name'],'DEPARTMENT',employee['department'],'SALARY',employee['salary']) 


def search():
    id=int(input("enter the employee id:"))
    found=False
    for employee in employees:
        if employee["ID"]==id:
            print("ID",employee['ID'],'NAME',employee['name'],'DEPARTMENT',employee['department'],'SALARY',employee['salary'])
            found=True
    if not found:
        print("Employee data is not found!!!")

def delete():
    id=int(input("enter the employee id:"))
    if not employees:
        print("No Employee records found!!")
    else:   
        for employee in employees:
            if employee["ID"]==id:
              employees.remove(employee)
            print("\nEmployee deleted succesfully-> ")

def salary():
    id=int(input("enter the employee id:"))
    for employee in employees:
        Salary=int(input("enter employee new salary"))
        employee['salary']=Salary
        print("employee salary is update succesfully!!:")

while True:
    print("\n press-1 for add employee:\n press-2 for display the Records: \n press-3 for delete employee Records: \n press-4 for search the employee: \n press-5 for update the employee salary: \n press-6 for exit the program:") 
    choice=int(input("enter the your choice:"))
    if choice==1:
        add_employee()
    elif choice==2:
        display()
    elif choice==3:
        delete() 
    elif choice==4:
        search() 
    elif choice==5:
        salary() 
    elif choice==6:
        print("Good bye->!!") 
        exit(0) 
    else:
        print("Invalid choice!!")                   

    