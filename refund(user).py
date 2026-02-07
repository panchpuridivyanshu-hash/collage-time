from Room_booking import *


room_price = 5000

while True:
    print("\n----- oyo room Hotel Booking Menu -----")
    print("---------Room Price=5000--------")
    print("Press 1 for Room Booking (Full Payment)")
    print("Press 2 for Room Booking (Advance Payment)")
    print("Press 3 to Cancel Booking and Get Refund")
    print("Press 4 to Display Booking List")
    print("Press 5 to Exit")

    
    choice = int(input("Enter your choice: "))
    

    if choice == 1:
        username = input('Enter your username: ')
        book_room(username, room_price)
    elif choice == 2:
        
        username = input('Enter your username: ')
        advance_amount = int(input("Enter the advance payment: "))
        advance_booking(username, advance_amount)
    elif choice == 3:
        user = input('Enter your username: ')
        refund(user)
    elif choice == 4:
        display(booking)
    elif choice == 5:
        print("Exiting the website. Goodbye!")
        break
    else:
        print("Invalid choice! Please enter a number between 1 and 5.")
