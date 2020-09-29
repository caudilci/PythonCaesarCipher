
def encrypt(str, shift):
    encryptedStr = ''
    for c in str:
        relativeShift = (ord(c)-ord(' ') + shift) % 95
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
    while(True):
        shift = input("Please provide a shift\n")
        if(int(shift) > 0):
            return int(shift)
        else:
            print("Invalid Shift\n")

def main():
    userIn = ''
    while(userIn != 'Q'):
        userIn = input("pick E, D, or Q\n")
        if(userIn == 'E'):
            print(encrypt(input('Message to encode\n'), getShift()))
        elif(userIn == 'D'):
            print(decrypt(input('Message to encode\n'), getShift()))

if __name__ == "__main__":
    main()