import math

Alphabet = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5,
            'G': 6, 'H': 7, 'I': 8, 'J': 9, 'K': 10, 'L': 11,
            'M': 12, 'N': 13, 'O': 14, 'P': 15, 'Q': 16,
            'R': 17, 'S': 18, 'T': 19, 'U': 20, 'V': 21,
            'W': 22, 'X': 23, 'Y': 24, 'Z': 25}

NumberRep = {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F',
             6: 'G', 7: 'H', 8: 'I', 9: 'J', 10: 'K', 11: 'L',
             12: 'M', 13: 'N', 14: 'O', 15: 'P', 16: 'Q',
             17: 'R', 18: 'S', 19: 'T', 20: 'U', 21: 'V',
             22: 'W', 23: 'X', 24: 'Y', 25: 'Z'}

#  This be my key yall.
a, b = 2, 2  # a = width b = height
Key_K = [[0 for x in range(a)]for y in range(b)]

Key1 = 9 #  Top left
Key2 = 4 #  Top right
Key3 = 5 #  Bottom left
Key4 = 7 #  Bottom right

#  This be the message I am encrypting :b:
Message = 'NEEDHELP'
M0 = Alphabet['N']
M1 = Alphabet['E']
M2 = Alphabet['E']
M3 = Alphabet['D']
M4 = Alphabet['H']
M5 = Alphabet['E']
M6 = Alphabet['L']
M7 = Alphabet['P']

#  Debug
#print (Message)

#  This is going to get verbose because I got
#  impatient and decided the remaining time
#  required to create a dynamic solution
#  was not worth the time investment.

def jennahaze ():

    emessage = None #  Final encrypted output message

    E0 = M0 ** Key1 #  First run
    E1 = M1 ** Key3
    E0 = E0 + E1
    print ('First range added: ', E0)
    E0 = E0 % 26
    E1 = NumberRep[E0]
    print ('First encrypted: ', E1)

    E2 = M2 ** Key2 #  Second run
    E3 = M3 ** Key4
    E2 = E2 + E3
    print('First range added: ', E2)
    E2 = E2 % 26
    E2 = NumberRep[E2]
    print('Second encrypted: ', E2)


#  Func call
jennahaze()

