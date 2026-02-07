print("-----------LOGIN PAGE----------------")
username=input("USERNAME:")
password=input("PASSWORD:")


if not username:
    print("username can not be blank!!!!")
elif not username.isalpha:  
    print("Error!! username can be contain only alfhabet") 
elif username!="admin":
    print("invalid username!!")   
else:
    len=len(password)

    if not password.isalnum:
        print("password must be conatain number characters and alfhabets!!!")    
    elif len>=20 and len<=8:
        print("password must be conatain 20 and minimun 8 charaters!!")  
    elif password!="admin@123":
        print("invalid password!!!!")   
    else:
        print("LOGIN successfulliy")   
print("thank you!!")           