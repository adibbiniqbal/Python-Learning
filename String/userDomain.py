email = input('Enter email: ')
idx = email.find('@')
user = email[0:idx:]
mail = email[idx+1::]
print(f'username: {user}')
print(f'domain: {mail}')