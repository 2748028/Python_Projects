import time

print ('Please enter "Add" if you wish to perform finite field addition: ')
print ('Enter "Sub" to perform finite field subtraction: ')
print ('Otherwise, enter "Mult" to perform finite field Multiplication: ')
Choice = input('Selection: ')

#----------------------------------------------------------#

if Choice == 'Add':
    #from operator import xor

    print ('Please be prepared to enter your two Polynomial arguments in integer form.')
    print ('I.E. Poly X+1 == Int 3, Poly X^2+X == Int 6.')
    time.sleep(4) #  Re-enable for distribution.

    AdditionValue1 = input('Please Enter An Integer Field Value (A) Between <0 - 255>: ')
    AdditionValue1 = int(AdditionValue1)

    if AdditionValue1 > 255 or AdditionValue1 < 0:
        print ('Please Enter An Value (A) Within The GF2^8 Field.')
        quit()
    else:
        AdditionValue2 = input('Please Enter An Intger Field Value (B) Between <0 - 255>: ')
        AdditionValue2 = int(AdditionValue2)
        if AdditionValue2 > 255 or AdditionValue2 < 0:
            print ('Please Enter An Value (B) Within The GF2^8 Field.')
            quit()


    print ('Input Value A: ', AdditionValue1)
    print ('Input Value B: ', AdditionValue2)

    print ('Converting To Binary.')

    BinAddVal1 = AdditionValue1
    BinAddVal1 = bin(BinAddVal1)[2:].zfill(8)

    BinAddVal2 = AdditionValue2
    BinAddVal2 = bin(BinAddVal2)[2:].zfill(8)

    print ('Binary Value A: ', BinAddVal1, 'Binary Value B: ', BinAddVal2)

    print ('XORing Binary Input.')

    #  Two variables are XOR'd and then written to the string.
    XOR = int(BinAddVal1, 2) ^ int(BinAddVal2, 2)
    print ('XOR Product: Integer Value: ', XOR)
    XOR = bin(XOR)[2:].zfill(8)
    print ('XOR Product Binary Value: ', XOR)
    quit()

#----------------------------------------------------------#

if Choice == 'Sub':
    # from operator import xor
    import time

    print('Please be prepared to enter your two Polynomial arguments in integer form.')
    print('I.E. Poly X+1 == Int 3, Poly X^2+X == Int 6.')
    time.sleep(4)  # Re-enable for distribution.

    AdditionValue1 = input('Please Enter An Integer Field Value (A) Between <0 - 255>: ')
    AdditionValue1 = int(AdditionValue1)

    if AdditionValue1 > 255 or AdditionValue1 < 0:
        print('Please Enter An Value (A) Within The GF2^8 Field.')
        quit()
    else:
        AdditionValue2 = input('Please Enter An Integer Field Value (B) Between <0 - 255>: ')
        AdditionValue2 = int(AdditionValue2)
        if AdditionValue2 > 255 or AdditionValue2 < 0:
            print('Please Enter An Value (B) Within The GF2^8 Field.')
            quit()

    print('Input Value A: ', AdditionValue1)
    print('Input Value B: ', AdditionValue2)

    print('Converting To Binary.')

    BinAddVal1 = AdditionValue1
    BinAddVal1 = bin(BinAddVal1)[2:].zfill(8)

    BinAddVal2 = AdditionValue2
    BinAddVal2 = bin(BinAddVal2)[2:].zfill(8)

    print('Binary Value A: ', BinAddVal1, 'Binary Value B: ', BinAddVal2)

    print('XORing Binary Input.')

    #  Two variables are XOR'd and then written to the string.
    XOR = int(BinAddVal1, 2) ^ int(BinAddVal2, 2)
    print('XOR Product: Integer Value: ', XOR)
    XOR = bin(XOR)[2:].zfill(8)
    print('XOR Product Binary Value: ', XOR)
    quit()

#----------------------------------------------------------#
#Initially I attempted this with two loops that would first create the powers, then sift through the output
#for duplicates, de-duped, and then XOR'd until I had, what I thought to be, the correct output.
#I scrapped this and attempted a function based approach instead due to too many road-blocks.

#Ensures that both values are padded equal in length in-case of different sized input.
def ProductPadding(XInput, YInput):
    Low = ""
    High = ""

    if (len(XInput) < len(YInput)):
        Low = XInput
        High = YInput
    else:
        Low = YInput
        High = XInput

    Padded = len(High) - len(Low)

    for i in range(0, Padded):
        Low = '0' + Low

    return Low, High

def DecimalAddition(XInput, YInput):
    i = len(XInput) - 1
    HumpOver = 0
    z = ""

    while (i >= 0):
        if (XInput[i] == '.'):
            z = '.' + z
            i -= 1
            continue
            
        t = int(XInput[i]) + int(YInput[i]) + HumpOver
        
        if (t == 0 or t == 2):
            z = '0' + z
        else:
            z = '1' + z

        if (t == 3 or t == 2):
            HumpOver = 1
        else:
            HumpOver = 0

        i -= 1

    return z, HumpOver

def Addition (XInput, YInput):
    XInput, YInput = ProductPadding(XInput, YInput)
    z, HumpOver = DecimalAddition(XInput,YInput)

    if (HumpOver == 1):
        z = str(HumpOver) + z

    return z

#Removes decimal input need for interation. Whilst logically keeping track of it.
def BinMult(XInput, YInput):

    decimal = None

    if ('.' in XInput):
        decimal = len(XInput) - 1 - XInput.index('.')
        XInput = XInput.split('.')
        XInput = XInput[0] + XInput[1]

    if ('.' in YInput):

        if (decimal != None):
            decimal += len(YInput) - 1 - YInput.index('.')

        else:
            decimal = len(YInput) - 1 - YInput.index('.')

        YInput = YInput.split('.')
        YInput = YInput[0] + YInput[1]

    i, x = len(XInput) - 1, 0
    result = ""

    while ( i >= 0 ):
        z = ""

        if( XInput[i] == '0'):
            i -= 1

        else:
            for j in range(0, x):
                z += '0'

            z = YInput + z
            result = Addition(result,z)
            i -= 1

        x += 1

    z = result[0:len(result) - decimal]
    z += '.'
    z += result[len(result) - decimal:]

    return z

if Choice == "Mult":

    print('Please be prepared to enter your two Polynomial arguments in integer form.')
    print('I.E. Poly X+1 == Int 3, Poly X^2+X == Int 6.')
    time.sleep(4)

    AdditionValue1 = input('Please Enter An Integer Field Value (A) Between <0 - 255>: ')
    AdditionValue1 = int(AdditionValue1)

    if AdditionValue1 > 255 or AdditionValue1 < 0:
        print('Please Enter An Value (A) Within The GF2^8 Field.')
        quit()
    else:
        AdditionValue2 = input('Please Enter An Integer Field Value (B) Between <0 - 255>: ')
        AdditionValue2 = int(AdditionValue2)
        if AdditionValue2 > 255 or AdditionValue2 < 0:
            print('Please Enter An Value (B) Within The GF2^8 Field.')
            quit()

    print('Input Value A: ', AdditionValue1)
    print('Input Value B: ', AdditionValue2)

    print('Converting To Binary.')

    BinAddVal1 = bin(AdditionValue1)[2:].zfill(8)
    print (BinAddVal1)
    BinAddVal2 = bin(AdditionValue2)[2:].zfill(8)
    print(BinAddVal2)

    BinAddVal1 = BinAddVal1
    BinAddVal2 = BinAddVal2

    print ('Please enter the two above binary strings with a "." at the end. '
           'This is needed because float types cannot be iterated without a decimal point.')

    BinVal3 = input('First Value w/".": ')
    BinVal4 = input('Second Value w/".": ')
    MultResult = BinMult (BinVal3, BinVal4)

    print ('Binary Multiplication Product: ', MultResult)

    print ('Checking To See If Output Is Within The field.')

    PresentMultLength = len(MultResult)
    XORCount = 0
    MultResult = MultResult.replace(".", "")
    XOROp = MultResult
    Irreductible = bin(255)[2:].zfill(8)
    print ('nut', Irreductible)

    print ('big ol test', XOROp)
    if (PresentMultLength <= 8):
        print ('Final Field Value: ', MultResult)
    else:
        print ('XORing Extended Field:')
        while PresentMultLength > 8:
            print ('Present XOR Process Count: ', XORCount)

            XOROp = int(XOROp) % int(Irreductible)
            print('XOR Product: Integer Value: ', XOROp)
            XOROp = bin(XOROp)[2:].zfill(8)
            Amount = str(XOROp)
            print('XOR Product Binary Value: ', XOROp)

            XORCount = XORCount + 1
            PresentMultLength = len(Amount)
            print ('present length', PresentMultLength)
        quit()

    quit()

#----------------------------------------------------------#

if Choice != 'Add' or 'Sub' or 'Mult':
    print ('Please enter an accepted input value. ')
    quit()
