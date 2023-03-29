# Initial configs
C1 = 0
C2 = 0

q = 71
print ("q: ", q)
prim = 7
print ("Prim root: ", prim)
# My dude bob's creds
Bobk = 2
print ("B's K Val: ", Bobk)
BobPublic = 3
print ("B's public Y: ", BobPublic)
Unencrypted = 30
print ("Unencrypted (message): ", Unencrypted)

BobK = BobPublic ** Bobk
BobK = BobK % q
print ("Bob's 'K' Value: ", BobK)
C1 = prim ** Bobk
C1 = C1 % q
print ("C1 value: ", C1)

C2 = BobK * Unencrypted
C2 = C2 % q
print ("C2 value: ", C2)
print ("Cipher'd value: (", C1, ")(", C2,")")

# Now we have to figure out some missing values using the provided C1 value.

C1 = 59

for x in range(0, q):

    if (prim ** x) % q == 59:
        y = x
        break

BigK = BobPublic ** y
BigK = BigK % q
print ('New "K" value: ', BigK)
C2 = BigK * Unencrypted
C2 = C2 % q
print ("New C2 value: (", C2, ")")


