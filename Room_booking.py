booking={}
def book_room(user,ammount):#room booking information
   if user in booking:
      print(f'Error!! {user} already book the room')
   else:
     booking[user]={'type':'full','amount':ammount}
     print(f'room succesfull book for {user} with full payment of {ammount}')

def advance_booking(user,advance_booking):
   if user in booking:
       print(f'Error!! {user} already book the room')

   else:    
      booking[user]={'type':'full','amount':advance_booking}
      print(f'room succesfull book for {user} with full payment of {advance_booking}')
    
def refund(user):
    if user in booking:
        user_booking = booking.pop(user)
        if user_booking['type'] == 'full':
            refund_amount = user_booking['amount'] * 0.9
        else:
            refund_amount = user_booking['amount'] * 0.8
        print(f"Refund of {refund_amount} processed for {user}.")   
    else:
        print(f"Error!! No booking found for {user}")
            

def display(booking):
     print(booking)