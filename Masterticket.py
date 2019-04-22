
TICKET_PRICE = 10

tickets_remaining = 100

while tickets_remaining >= 1:

  # run this code continuously until we run out of tickets
  
  # output how many ticke ar remaining using the tickets_remaining variable
  print("there are {} tickets remaining".format(tickets_remaining))
  # gather the user's name and asign it to a new variable
  name = input("what is your name?")
  
  # prompt the user by name and ask how many tickets they would like
  
  num_tickets = input("how many tickets would you like {}?".format(name))
  try:                                                                   
     num_tickets = int(num_tickets)
    # raise a ValueError if the request is for more tickets than available
     if num_tickets > tickets_remaining:
          raise ValueError("there are only {} tickets remaining".format(tickets_remaining)) 
  except ValueError as err: 
      print("oh no we ran into an issue please try again ".format(err))
  # calculate the price(number of tickets they want multiplied by the price) and assign it to a variable
  else:  
    amount_due = num_tickets * TICKET_PRICE
    # output the price to the screen
    print("amount due is {}".format(amount_due))
    
    # prompt user if they want to proceed  Y/N ?
    
    should_proceed = input (" do you want to proceeed? Y/N")
    if should_proceed.lower() == "y":
             # print out to the screen "SOLD" to confirm the purchese 
        print("SOLD")
        
            # then decrement the number of tickets remaining by the number of tickets purchased
        tickets_remaining -= num_tickets
    else:
             #otherwise ...
            print("thank you anyway {}.".format(name))
           # thank them by name 
    # Notify the user when there are tickets left 
    
print(" sorry they all sold out")