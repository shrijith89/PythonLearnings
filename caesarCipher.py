myList = []

string = input("Enter the string")
myList = list(string)
encryptedString = ''


def shiftFunction (shift):
    encryptedString = ''
    for i in myList:
        encryptedCharacter = ord(i) + shift
        encryptedString += chr(encryptedCharacter)
    return encryptedString


print(f"The encrypted string is {shiftFunction(3)}")
