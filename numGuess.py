import random
a = int(input('enter range beginning: '))
b = int(input('enter range ending: '))
n = random.randint(a,b)
count = 0
guess = -2**31
while guess!=n:
    guess =  int(input('enter a guess: '))
    if guess < n:
        print('number is higher')
    elif guess > n:
        print('number is lower')
    count += 1
print(f'your guess is right, you took {count} guesses')