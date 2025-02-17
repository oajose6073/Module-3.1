from pprint import pprint
account_balance = {}
with open("account_balances.txt", "r") as file:
    for line in file:
        key, value = line.strip().split('|')
        account_balance[key] = int(float(value))
pprint(account_balance)
balance = list(account_balance.values())
print(balance)

updated_balances = {}
interest =[]
for key, amount in account_balance.items():
    if amount < 1000 :
        rate = 0.01
        
    elif amount < 5000 and amount >= 1000 :
        rate = 0.025
        
    elif amount > 5000 :
        rate = 0.05
        
    if amount < 0 :
        rate = -0.10

    monthly_interest = (amount*rate)/12
    interest.append(monthly_interest)

    updated_balances [key] = f"{monthly_interest + amount: .6f}"
   
print("Interest:", interest)
pprint(updated_balances)