#Temperature Converter – Convert temperatures between Celsius, Fahrenheit, and Kelvin
def celsius(fahre,kelvin):
    celsiu=(fahre-32)*(5/9)
    celsius=kelvin-273.15
    print(f"temprature fahrenhitin to celsiusc is : {celsiu}c")
    print(f"temprature kelvin to celsius is {celsius}c")

def fahrenheit(celsius,kelvin):
    fahre=(celsius*9/5)+32
    fahrenheit=(kelvin-273.15)*9/5+32
    print(f"temprature celsius to fahrenhitin is  : {fahre}f")
    print(f"temprature kelvin to fahrenhitin is {celsius}c")

def kelvin(celsius,fahre):
    kel=celsius+273.15
    kelvin=(fahre-32)*5/9+273.15
    print(f"temprature celsius to fahrenhitin is  : {fahre}f")
    print(f"temprature kelvin to fahrenhitin is {celsius}c")

while True:
    print("press-1 for convert fahrenheit and kelvin to celsius:")
    print("press-2 for convert celsius and kelvin to fahrenheit:")
    print("press-3 for convert fahrenheit and celsius to kelvin:")
    print("press-4 for exit the program!!")
   
    choice=int(input("enter the your choice:"))
    if choice==1:
        f=float(input("enter the Temperature in fahrenheit:"))
        k=float(input("enter the Temperature in kelvin:"))
        celsius(f,k)
    elif choice==2:  
        c=float(input("enter the Temperature in celsius:"))
        k=float(input("enter the Temperature in kelvin:"))
        fahrenheit(c,k)  
    elif choice==3:
            c=float(input("enter the Temperature in celsius:"))
            f=float(input("enter the Temperature in fahrenheit:"))
            kelvin(c,f)
    elif choice==4:
         print("Good bye!!") 
         exit(0)    
    else:
         print("invalid choice!!")        