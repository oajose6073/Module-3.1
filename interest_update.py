from pprint import pprint
account_balance = {}
with open("account_balances.txt", "r") as file:
    for line in file:
        key, value = line.strip().split('|')
        account_balance[key] = (int(float(value)))
pprint(account_balance)
