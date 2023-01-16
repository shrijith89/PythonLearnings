import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to password generator")
lettersn = int(input("How many letters"))
numbersn = int(input("How many numbers"))
symbolsn = int(input("How many symbols"))

length = lettersn+numbersn+symbolsn

passwordlist = random.choices(letters,k=lettersn) + random.choices(numbers,k=numbersn) + random.choices(symbols,k=symbolsn)
password = ''.join(passwordlist)
print(f"The password is {password}")
print(f"The randomized password is {''.join(random.choices(password,k=length))}")
