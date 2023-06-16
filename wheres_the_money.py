#print out program header
print('-' * 29)
print('-' * 5, 'WHERE\'S THE MONEY', '-' * 5)
print('-' * 29)
#inputs to prompt a user for how much they make and what they spend it on
ansal = input('What is your annual salary? \n')
#make sure input is a numeric value
if ansal.isnumeric() == False:
    print('Must enter positive integer for salary.')
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
#convert ansal into a float type variable named ansa
#trav to tra
#the others will be converted later
ansa = float(ansal)
tra = float(trav)
#space
print(' ')
#line breeak for results
print('-' * 66)
print('See the financial breakdown below, based on a salary of $' + str(ansal))
print('-' * 66)
#create formulas to turn inputs into their yearly figures (travel already is)
mr = float(mmren) * 12 #mr stands for mortgage rent
bil = float(bills) * 12 #bil is short for bills
fo = float(food) * 52 #fo is short for food
#for the tax section
if ansa <= 15000:
    tax = 0.10
elif ansa > 15000 and ansa <= 75000:
    tax = 0.20
elif ansa > 75000 and ansa <= 200000:
    tax = 0.25
elif ansa > 200000:
    tax = 0.30
#formula for any extra funds
extra = ansa - (mr + bil + fo + tra + tax) 
#create formulas to determin what % this is out of the annual salary (exluding tax)
#pre stands for precentage and varibal names were reused to more easily match
premr = (mr / ansa) * 100.00
prebil = (bil / ansa) * 100.00
prefo = (fo / ansa) * 100.00
pretrav = (tra / ansa) * 100.00
pretax = (tax / ansa) * 100.00
preex = (extra / ansa) * 100.00
#Now to format the results 
#naming convention for these variabls is to reuse the name with _f
#_f is short for formating
mr_f = format(mr, '15,.1f')
bil_f = format(bil, '15,.1f')
fo_f = format(fo, '15,.1f')
tra_f = format(tra, '15,.1f')
tax_f = format(tax, '15,.1f')
extra_f = format(extra, '15,.1f')
#print results test
print('|', format('mortgage/rent', '>15'), '| $', mr_f, '|')