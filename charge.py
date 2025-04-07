# I Ravleen Singh, 000933596, certify that this work is my own effort and that I have not allowed anyone else to copy from it.

import random

def calculate_change(payment, amount):

  change = payment - amount
  
  if change == 0:
    return {"dollars": 0, "quarters": 0, "dimes": 0, "nickels": 0}


  change = round(change * 20) / 20


  dollars = 0
  quarters = 0
  dimes = 0
  nickels = 0

# for round off
  if change >= 1.00:
    dollars += int(change // 1.00)
    change -= dollars * 1.00

  if change >= 0.25:
    quarters += int(change // 0.25)
    change -= quarters * 0.25

  if change >= 0.10:
    dimes += int(change // 0.10)
    change -= dimes * 0.10

  if change >= 0.05:
    nickels += int(change // 0.05)
    change -= nickels * 0.05


  return {
      "dollars": dollars,
      "quarters": quarters,
      "dimes": dimes,
      "nickels": nickels,
  }


# payment using random 
payment = random.randint(0,20) + round( random.randint(0,100)/100, 2 ) 

print("Total Bill: ", payment)

print("\n")
# enter amount you paid
amount = float(input("Enter the amount paid: "))

# you paid less amount than payment(bill)  for example: if payment is $5.78 and amount is $5
if amount< payment:
    print("Amount Paid is Less Then Bill Amount")
    
else:
    # you paid more or same amount than payment(bill)
    change = calculate_change(amount, payment)
    
    # if payment is $5.78 and amount is $5.78
    if change == {"dollars": 0, "quarters": 0, "dimes": 0, "nickels": 0}:
      print("No change is owed.")
      
    else:
    #   if payment is $5.78 and amount is $10
      print("\nYour change is:")
      
      if change["dollars"] > 0:
        print(f"{change['dollars']} dollar(s)")
        
      if change["quarters"] > 0:
        print(f"{change['quarters']} quarter(s)")
      
      if change["dimes"] > 0:
        print(f"{change['dimes']} dime(s)")
      
      if change["nickels"] > 0:
        print(f"{change['nickels']} nickel(s)")
        
        
    
