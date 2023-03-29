import sys

# a ^ p a mod p
a = 45 # Random integer
p = 2047 # Integer we are testing the prime-ness of (99.9% accuracy)

Prod1 = a ** p
print ('Product: ', Prod1)
Prod2 = Prod1 % p
print ('If == 1 then == Prime, Else composite: ', Prod2)

# Therefore 2047 fails fermat's test as it is not a prime.