#
#Author: Kyle Loflin
#Class: CSC 110
#Description: this is a madlib program that will also solve math problems
#
#list of inputs (string)
r1 = input('Name of teacher: \n')
r2 = input('A female student: \n')
r3 = input('A male student: \n')
#list of inputs (numbers)
n1 = int(input('A whole number: \n'))
n2 = int(input('Another whole number \n'))
#math formulas
c2 = (n1 ** 2) + (n2 ** 2)
ra = n1 * n2
#space
print(' ')
#print results
print(r1, 'entered the classroom and began to give a lecture.')
print('\"Give me some numbers for variables A and B!\"', r1, 'shouted.')
print('\"' + str(n1) + '\"', r2, 'replied.')
print('Immediately after,', r3, 'followed up with', '\"' + str(n2) + '\"')
print(r1, 'then replied: \"Great, now plug those into the pythagorean theroem. What is C?\"')
print('There were a few moments of silence, then', r2, 'said:')
print('\"' + str(c2) + '\"')
print('\"Correct. Now, what is the area of a rectangle with A and B and the length of the sides?\"')
print('\"' + str(ra) + '\"', r3, 'eclaimed.')
print('Good, Class dismissed')