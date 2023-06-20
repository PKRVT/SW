string = input('Enter string:\n')
i = len(string) - 1
count = 1
while count != 0 or count > 0 or count < 1:
    if string[i] == ')':
        count += + 1
    while count != 0:
        if string[i] == '(':
            count += - 1
if count == 0:
    print('Parentheses balanced')
else:
    print('Parentheses unbalanced')