bill = int(input("What is your total bill"))
tipPercentage = int(input("Enter the percentage of tip amount"))
tipAmount = (tipPercentage/100)*bill

finalBill = bill-tipAmount
dividedByhowMany = int(input("How many people to be divided to"))
print(f"The amount for each person is {finalBill/dividedByhowMany}")