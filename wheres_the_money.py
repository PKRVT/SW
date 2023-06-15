#print out program header
print('-' * 29)
print('-' * 5, 'WHERE\'S THE MONEY', '-' * 5)
print('-' * 29)
#inputs to prompt a user for how much they make and what they spend it on
ansal = input('What is your annual salary? \n')
#make sure input is a numeric value
if ansal.isnumeric() == False:
    print('Must enter positive integer for annual salary')
    exit()
mmren = input('How much is your monthly mortgage or rent? \n')
if mmren.isnumeric() == False:
    print('Must enter positive integer for mortgage or rent.')
    exit()
bills = input('What do you spend on bills monthly? \n')
if bills.isnumeric() == False:
    print('Must enter positive integer for bills.')
    exit()
food = input('What are your weekly grocery/food expenses? \n')
if food.isnumeric() == False:
    print('Must enter positive integer for food.')
    exit()
trav = input('How much do you spend on travel annually? \n')
if trav.isnumeric() == False:
    print('Must enter positive integer for travel.')
    exit()
#line breeak for results
print('-' * 66)
print('See the financial breakdown below, based on a salary of $' + str(ansal))
print('-' * 66)
#print results
