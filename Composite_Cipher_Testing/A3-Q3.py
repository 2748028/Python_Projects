#Generates a pub and priv key. As well as performs RSA encryption/decryption.
#Commented this section out as it's functionality was confusing/inaccurate.
#import sys
#sys.setrecursionlimit(1000000)  # long type

#import random

#Primes =[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37,
#        41]
#n = 0

#p = int(random.choice(Primes))
#print ('p: ', p)

#q = int(random.choice(Primes))
#print ('q: ', q)

#pn = p - 1
#qn = q - 1
#n = int(pn * qn)
#print ('(mod) n: ', n)

#e = random.randint(2, 100)
#e = random.randint(2, 150)

#PublicKey = [7, 187]
#print ('(exponent) e: ', e)
#Inverse = None

# 7^-1 mod "x" Pre-computed by hand to save time on programming a whole multiplicative inverse function.
#print ('Calculate ',e,'^-1 mod:', n)

#d = input('Please input the mult inverse product: ')
#d = int(d)
#print ('(mult inverse) "d" == ', d)
#PrivateKey = [d, n]
#PublicKey = [e, n]
#PrivateKey = [23, 187]

#print ('Public Key: ', PublicKey)
#print ('Private Key: ', PrivateKey)

#plaintext1 = input ('Enter a plaintext value (numeric preferred): ')
#plaintext1 = int(plaintext1)

#print ('Encrypting...')
#plaintext1 = plaintext1 ** PublicKey[0]
#plaintext2 = plaintext1 % PublicKey[1]
#print ('Ciphertext: ', plaintext2)

#print ('Decrypting...')
#decrypted1 = plaintext2 ** PrivateKey[0]
#decrypted2 = decrypted1 % PrivateKey[1]
#print ('Plaintext: ', decrypted2)

# Cleaner implementation that gives up dynamic inputs for simpler/cleaner code.
M = 69
print ("Plaintext: ", M)
p = 11
print ('p: ', p)
q = 13
print ('q: ', q)
e = 11
print ('e: ', e)

def MultInv (a,c):
    for x in range(1, c):
        if a * x % c == 1:
            print ('Found an inverse my dude.')
            return x

n = p * q
print ('n: ', n)

n2 = (p - 1) * ( q - 1)
d = MultInv(e, n2)

# Encryption
C = M ** e
C = C % n
print ("Encrypted input: %d" % C)
# Decryption
P = C ** d
P = P % n
print ("Converted to plaintext: %d" % P)

