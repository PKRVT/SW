#get and validate inputs
string1 = input('Hit string: \n')
if len(string1) > 3 or len(string1) % 4 != 0:
    print('Please provide a valid hit string.')
string2 = input('Marker: \n')
if len(string2) != 1:
    print('Please provide a valid marker')