#input for water temp
x = int(input('Temperature in fahrenheit: \n'))
#if statement for water states
if x >= 212:
    print('Steam')
elif x < 212 and x > 32:
        print('Water')
else:
      print('Ice')