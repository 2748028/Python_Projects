#import numpy as np

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

Key1 = Key_K[0][0] = 9 #  Top left
Key2 = Key_K[1][0] = 4 #  Top right
Key3 = Key_K[0][1] = 5 #  Bottom left
Key4 = Key_K[1][1] = 7 #  Bottom right

#  This be the message I am encrypting b
Message = 'NEEDHELP'

#  Debug
#print (Message)

#  This is going to get verbose because I got
#  impatient and did not feel like making a
#  dynamic solution.

def JennaHaze ():
    message = None #  Final output message
    i = 0 #  Counter for first message appending loop.
    messagecontents = [] #

    #for i in range(len(PlainMessage)): #  Adds the list of letters to be encrypted to a user display variable.
    #    messagecontents.append (PlainMessage[i])
    #    i += 1
    #    message = ''.join(messagecontents)
    #print (message)

    temp1 = None
    count = 0 #  Variable used to ensure only two letters are encrypted at a time.
    while (count < 8): #  Forgive me for my static programming ways Stallman.
        for i, c in enumerate(Message):
            temp1 = i ^ Key1
            #modcalc1 = temp1 + temp2
            #print (modcalc1)
            #encrypted1 = modcalc1 % 26
            #print (NumberRep[encrypted1])
            count += 1

    val_of_char = ord('C') - ord('A')
    #print (val_of_char)

#  Func call
JennaHaze()