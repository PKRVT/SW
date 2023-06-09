#establish variables for width and height
w = int(input('Rectangle width: \n'))
h = int(input('Rectangle height: \n'))

row = '#' * w + '\n'
print(row * h, end='')
