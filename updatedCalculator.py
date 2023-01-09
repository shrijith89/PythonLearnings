dictionary = {}


def add(num1, num2):
    return num1 + num2


def subtract(num1, num2):
    return num1 - num2


def multiply(num1, num2):
    return num1 * num2


def divide(num1, num2):
    return num1 / num2


dictionary = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide
}

def func():
    result = 0
    letter = 'y'
    number1 = int(input("Enter the number 1"))
    operationSymbol = input("Pick an Operation Symbol")
    number2 = int(input("Enter the number 2"))
    calculation_Function = dictionary[operationSymbol]
    result = calculation_Function(number1, number2)
    while(letter=='y'):
        letter = input("Do you want to continue the operation? (y or n)?")
        if letter == 'n':
            break
        else:
            operationSymbol = input("Enter the next set of operation to perform")
            number3 = int(input("Enter the number"))
            calculation_Function = dictionary[operationSymbol]
            resultUpdated = calculation_Function(number3,result)
            print(resultUpdated)

func()