#2.Calculator – A simple calculator that can perform basic arithmetic operations
def calculator(num1,num2):
    while(1):
        print("press-1 for Addition(+):")
        print("press-2 for subtrection(-):")
        print("press-3 for Multiplication(*):")
        print("press-4 for division(/):")
        print("press-5 for Module(%):")
        calc=int(input("enter your choice:"))
        if calc==1:
          return num1+num2
        elif calc==2:
          return num1-num2
        elif calc==3:
          return num1*num2
        elif calc==5:
          return num1%num2
        elif calc==4:
           if num2==0:
              return "operation can not posible"
           else:
              return num1/num2    
        else:
            return "invalid choice!!"    
print("=======CALCULATER=======")    
a=int(input("NUM1:"))
b=int(input("NUM2:"))   
result=calculator(a,b) 

print("=========RESULT:",result,"==============")
