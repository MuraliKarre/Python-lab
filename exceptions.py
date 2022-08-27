try:
    age = int(input('Age :'))
    income = 2000
    risk = income / age
    print(age)
except ValueError:
    print('Invalid value')
except ZeroDivisionError:
    print('Age cannot be Zero')