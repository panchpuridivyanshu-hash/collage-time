#3.To-Do List – A simple task manager that allows users to add, view, and delete tasks.
list=[]

def create_list(list):
    if len(list)<0:
        insert_task(list)

def show_list(list):
    print("\n To-Do List:")
    for i in range(0,len(list)):
        print(i,list[i])

def insert_task(list):
    task=input("enter the task:") 
    list.append(task)
    print("task added!!!")  

def remove_task(list):
    index=int(input("enter that index number which task will you remove:"))
    if index<0 and index>len(list):
        print("invalid task number:")   
    else:
        list.pop(index) 
        print("task removed")  



while True:
    print("Press-1 create list:")
    print("press-2 add task:")
    print("press-3 remove task:")
    print("press-4 display task list:")
    print("press-5 exit this program")
    choice=int(input("enter the choice:"))

    if choice==1:
        create_list(list)
    elif choice==2:
        insert_task(list)
    elif choice==3:
        remove_task(list)  
    elif choice==4:
        show_list(list) 
    elif choice==5: 
        print("Exiting list. Goodbye!")
        break
    else:
        print("invalid choice!!!")   