amount = int(input('print bill amount: '))
if amount<=1000:
    amount = amount - amount*10/100
elif amount>=1000 and amount<=5000:
    amount = amount - amount*15/100
elif amount>=5000 and amount<=10000:
    amount = amount - amount*20/100
else:
    amount = amount - amount*25/100
print(f'amount = {amount}')

