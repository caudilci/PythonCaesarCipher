
def encrypt(str, shift):
    encryptedStr = ''
    for c in str:
        relativeShift = (ord(c)-ord(' ')+ shift) % 95
        encryptedChar = chr(ord(' ') + relativeShift)
        encryptedStr += encryptedChar
    return encryptedStr

def decrypt(str, shift):
    decryptedStr = ''
    for c in str:
        relativeShift = (ord(c)-ord(' ') - shift) % 95
        decryptedChar = chr(ord(' ') + relativeShift)
        decryptedStr += decryptedChar
    return decryptedStr

def getShift():
    return 0

print(encrypt('My dog eats shit.', 1))
print(decrypt('Nz!eph!fbut!tiju/', 1))