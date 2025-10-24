# example-1 
# def add(num1, num2):
#     addt = num1 + num2
#     return addt

# def sub(num1, num2):
#     subt = num1 - num2
#     return subt

# def mul(num1, num2):
#     mult = num1 * num2
#     return mult

# num1 = float(input("enter first number: "))
# num2 = float(input("enter second munber: "))

# print(add(num1, num2))
# print(sub(num1, num2))

# print("example2")
# print(" ")

#example2

import sys

def add(num1, num2):
    addt = num1 + num2
    return addt

def sub(num1, num2):
    subt = num1 - num2
    return subt

def mul(num1, num2):
    mult = num1 * num2
    return mult

num1 = float(sys.argv[1])
operation = sys.argv[2]
num2 = float(sys.argv[3])


if operation.lower() in ["add", "addition", "plus", "sum"]:
    output = add(num1, num2)
    print(round(output))

if operation.lower() in ["sub", "subtraction", "minus"]:
    output = sub(num1, num2)
    print(round(output))


# for environment variable use - export apikeys="password".

# import os

# print(os.getenv("apitoken"))


# import sys


# num1 = float(sys.argv[1])
# operation = sys.argv[2]
# num2 = float(sys.argv[3])


# if operation == "add":
#     output = add(num1, num2)
#     print(round(output))

# if operation == "sub":
#     output = sub(num1, num2)
#     print(round(output))

