class AccountBalanceException(Exception):
    pass
balance = 10000
def withdraw(amount):
    global balance
    if balance - amount >= 0:
        balance -= amount
    else:
        raise AccountBalanceException('Account does not have sufficient money')

amount = int(input('enter amount: '))
try:
    withdraw(amount)
except AccountBalanceException as msg:
    print(msg)
else:
    print('withdrawn successfully, remaining balance:', balance)