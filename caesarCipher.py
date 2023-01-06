myList = []

string = input("Enter the string")
myList = list(string)
encryptedString = ''


for i in myList:
    encryptedCharacter = ord(i)+5
    encryptedString += chr(encryptedCharacter)

print(f"The encrypted string is {encryptedString}")