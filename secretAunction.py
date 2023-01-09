import os

aunction = {}
flag = True

while(flag == True):
    yourName = input("Enter your name")
    bidAmount = input("Enter the bid amount")
    bidPending = input("You still have a bid").lower()
    aunction[yourName] = bidAmount
    if bidPending == "no":
        flag = False
    max_value = max(aunction, key=aunction.get)
    print(max_value, aunction[max_value])