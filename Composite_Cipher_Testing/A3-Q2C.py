# Miller Rabin Test
# n - 1 = 2^k X m
# n = Number being tested against for primality.
# k = Iterated by a increment of one for each iteration.
# m = Product, must not be a decimal or the previous value must be tested.
import decimal
from random import randint

Originaln = 2047
n = 2047 - 1 # -1 whatever value entered.
CurrentProduct = None
k = 0
m = None
ProductOfTwo = 0
PreviousGood = 0
IsWhole = None

while CurrentProduct != True:
    ProductOfTwo = 2 ** k # 2^k
    m = n / ProductOfTwo # n / (2^k)
    print ('Product ==', m)
    IsWhole = (m).is_integer()

    if IsWhole == True:
        print ('"k" value: ', k)
        print ('You made it to the whole numbers group.')
        k = k + 1
        CurrentProduct == False
    else:
        print ('You reached the exit function!')
        k = k - 1
        ProductOfTwo = 2 ** k  # 2^k
        m = n / ProductOfTwo  # n / (2^k)
        print ('Last known whole: ', m, 'With k: ', k)
        CurrentProduct = True

print ('Congrats you made it to pt. 2')

# Step 2: 1 < a < n
a = 2
print ('Random "a" value: ', a)

# Step 3: bo = a^m (mod n)
print ("m: ", m)

APowerM = a ** m
print (APowerM)
APowerM2 = APowerM % Originaln
print (APowerM2)
