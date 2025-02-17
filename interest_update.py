from pprint import pprint       # I have to import pprint to have a pretty print

account_balance = {}
with open("account_balances.txt", "r") as file:
    for line in file:
        key, value = line.strip().split('|')        #Delimitter is "|"
        account_balance[key] = int(float(value))    #needed to convert value to integer
pprint(account_balance)
balance = list(account_balance.values())            # Listed the values of account balance 
print(balance)

updated_balances = {}
interest =[]
for key, amount in account_balance.items():
    if amount < 1000 :
        interest_rate = 0.01
        
    elif amount < 5000 and amount >= 1000 :
        interest_rate = 0.025
        
    elif amount > 5000 :
        interest_rate = 0.05
        
    if amount < 0 :
        interest_rate = -0.10

    monthly_interest = (amount*interest_rate)/12
    interest.append(monthly_interest)                       # Added the interest values to the empty list on Line 13.

    updated_balances [key] = f"{monthly_interest + amount: .6f}"    #Converted the balance to 6 decimal place.
   
print("Interest:", interest)
pprint(updated_balances)

with open("updated_balances_OA.csv", "w", newline='') as csvfile:       #Created a csv file without using DictWriter
    csvfile.write("Account,Balance\n")                                  #Made the header for my csv file to be Account and Balance
    for key, value in updated_balances.items():
        csvfile.write(f"{key},{value}\n")

import csv
with open('updated_balances_OA.csv', 'r') as file:                  #Imported the created csv file
    reader = csv.DictReader(file)
    for row in reader:
        print(row['Account'], row['Balance'])                       #printed the csv file 
