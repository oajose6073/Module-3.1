menu = ["D","W","Q"]
initial_balance = 4500

print("*" * 40)
print("PIXELL RIVER FINANCIAL".center(40))
print("ATM Simulator".center(40))
print("\n", f"Your current balance is: ${initial_balance:,.2f}".center(40))
print("\n", f"Deposit: {menu[0]}".center(40))
print(f"Withdrawal: {menu[1]}".center(40))
print(f"Quit: {menu[2]}".center(40))
print("*" * 40)

import os                                       #Import for clearing the screen
import time                                     #Import for pausing the screen for 3 sec
selection = " " 
while selection != 'Q':
    selection = input("\nEnter your selection: ").upper()               # This is to make sure the all both the upper and lower case of input works
    if selection not in menu:                     #conditional statement for selection that is not D, W or Q which is found in the list menu created on line 1
        print("\n", "*" * 40)
        print("INVALID SELECTION".center(40))
        print("*" * 40)
        time.sleep(3)
        os.system('cls' if os.name == 'nt' else 'clear')
        continue                                            #This is to skip the rest of the loop.

    elif selection == 'D':
        deposit_amount = int(input("\nEnter the transaction amount: "))
        initial_balance += deposit_amount                   #This is to add the amount deposit in line 27 to the balance of customer.
        print("\n","*" * 40)
        print(f"Your current balance is: ${initial_balance:,.2f}".center(40))
        print("*" * 40)
        time.sleep(3)
        os.system('cls' if os.name == 'nt' else 'clear')   

    elif selection == 'W':
        withdrawal_amount = int(input("\nEnter the transaction amount: "))
        if withdrawal_amount <= initial_balance:            #this is a conditional statement that states that the rest of the loop will only continue if customer have enough money in their account
            initial_balance -= withdrawal_amount            #This is to subtract the amount withdrawn in line 36 from the balance of customer.
            print("\n", "*" * 40)
            print(f"Your current balance is: ${initial_balance:,.2f}".center(40))
            print("*" * 40)
            time.sleep(3)
            os.system('cls' if os.name == 'nt' else 'clear')
                
        elif withdrawal_amount >= initial_balance:                      # A message will display if customer does not have enough money n their account
            print("\n", "*" * 40)
            print("INSUFFICIENT FUNDS".center(40))
            print( "*" * 40)
            time.sleep(3)
            os.system('cls' if os.name == 'nt' else 'clear')
    