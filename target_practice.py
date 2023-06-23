#main for the functions to connect in
def main():
    string1 = input('Hit string: \n')
    string2 = input('Marker: \n')
    input(string1, string2)
def input(s1, s2):
    '''this validate inputs from user'''
    if len(s1) > 3 or len(s1) % 4 != 0:
        print('Please provide a valid hit string.')
    if len(s2) != 1:
        print('Please provide a valid marker.')
main()