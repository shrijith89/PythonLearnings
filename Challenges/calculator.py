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

number1 = int(input("Enter the number 1"))
operationSymbol = input("Pick an Operation Symbol")
number2 = int(input("Enter the number 2"))

calculation_Function = dictionary[operationSymbol]
print(calculation_Function(number1, number2))
