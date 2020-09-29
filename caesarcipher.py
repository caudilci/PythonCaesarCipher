
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
    while(userIn != '3'):
        userIn = input("pick 1, 2, or 3\n")
        if(userIn == '1'):
            print(encrypt(input('Message to encode\n'), getShift()))
        elif(userIn == '2'):
            print(decrypt(input('Message to encode\n'), getShift()))

if __name__ == "__main__":
    main()