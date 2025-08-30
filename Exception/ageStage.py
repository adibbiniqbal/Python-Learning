class NegativeAgeException(Exception):
    pass


def stage(age):
    if age > 50:
        print('old')
    elif age > 18:
        print('young')
    elif age > 13:
        print('teen')
    elif age <= 13 and age >= 0:
        print('kid')
    else:
        raise NegativeAgeException('Age should be positive')
    
age = int(input('enter age: '))
try:
    stage(age)
except NegativeAgeException as msg:
    print(msg)