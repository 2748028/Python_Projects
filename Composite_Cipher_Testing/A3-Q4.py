CipherText = 16
CipherText = int(CipherText)
Product = 0
PublicKey = [5, 35]
PlainText = 0
ciphertext1 = 0
ciphertext2 = 0

while ciphertext2 != 16:
    print ('Encrypting...')
    ciphertext1 = PlainText ** PublicKey[0]
    ciphertext2 = ciphertext1 % PublicKey[1]
    print ('Ciphertext: ', ciphertext2)
    if ciphertext2 == 16:
        print ('Plaintext == ', PlainText)
    else:
        PlainText = PlainText + 1

