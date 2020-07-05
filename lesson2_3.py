# Task 3
month = int(input('Enter month: '))

if month <= 0 or month >= 13:
    print('Incorrect month')

elif month >= 3 and month <= 5:
    print('Spring')

elif month >= 6 and month <= 8:
    print('Summer')

elif month >= 9 and month <= 11:
    print('Autumn')

else:
    print('Winter')