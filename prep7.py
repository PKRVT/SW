#inputs for size and type of drink
size = input('Drink Size: \n')
dt = input('Drink type: \n')
#variables for the different sizes and types
if size == "large" and dt == 'regular':
    print('300 calories')
elif size == 'small' and dt == 'regular':
    print('150 calories')
elif size == 'large' and dt == 'diet':
    print('100 calories')
elif size == 'small' and dt == 'diet':
    print('50 calories')
elif dt == 'water':
    print('0 calories')