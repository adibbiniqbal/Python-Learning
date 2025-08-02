password = input('Enter password: ')
confirm = input('Enter password to confirm: ')
if password==confirm:
    print('Equal')
elif password.lower()==confirm.lower():
    print('Check for cases and try again')
else:
    print('Try again')