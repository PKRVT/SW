def main():
    print('----- Avatar -----')
    greet = input('Select an Avatar or create your own: \n')
    if greet == 'custom':
        print('Answer the following questions to create a custome avatar')
        hat_sty = input('Hat style ? \n')
        eye_char = input('Character for eyes ? \n')
        hair_len = input('Long hair (True/False) ? \n')
        arm_sty = input('Arm style ? \n')
        torso_len = input('Toroso length ? \n')
        leg_len = input('Leg length (1-4) ? \n')
        shoe_look = input('Shoe look ? \n')
        hat(hat_sty)
        hair(hair_len, eye_char)
        arm(arm_sty)
        torso(torso_len)
        leg(leg_len)
        shoe(shoe_look, leg_len)
def hat(hs):
    print('       ~-~')
    print('     /-~-~-\\')
    if hs == 'front':
        print('    /_______\\')
    elif hs == 'both':
        print(' ___/_______\\___')
    elif hs == 'right':
        print('    /_______\\___')
    elif hs == 'left':
        print(' ___/_______\\')
    else:
        print('    /_______\\')
def hair(hl, ec):
    if hl == 'True':
        print('   "|"""""""|"')
        print('   "| '+ec+'   '+ec+' |"')
        print('   "|   V   |"')
        print('   "|  ~~~  |"')
        print('   " \\_____/ "')
    elif hl == 'False':
        print('    |"""""""|')
        print('    | '+ec+'   '+ec+' |')
        print('    |   V   |')
        print('    |  ~~~  |')
        print('     \\_____/ ')
def arm(ars):
    print(' 0'+ars+ars+ars+ars+'|---|'+ars+ars+ars+ars+'0')
def torso(tl):
    count = 0 
    while count < len(tl):
        print('      |-X-|\n')
        count += 1
def leg(ll):
    print('      HHHHH')
    if ll == 1:
        print('     /// \\\\\\')
    elif ll == 2:
        print('     /// \\\\\\')
        print('    ///  \\\\\\')
    elif ll == 3:
        print('     /// \\\\\\')
        print('    ///  \\\\\\')
        print('   ///   \\\\\\')
    elif ll == 4:
       print('     /// \\\\\\')
       print('    ///  \\\\\\')
       print('   ///   \\\\\\')
       print('  ///    \\\\\\')
    elif ll == 5:
       print('     /// \\\\\\')
       print('    ///  \\\\\\')
       print('   ///   \\\\\\')
       print('  ///    \\\\\\')
       print(' ///     \\\\\\') 
def shoe(sl, ll):
    if ll == 1:
        print(sl+' '+sl)
main()