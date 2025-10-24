#example1-functions
num1 = float(input("enter first number: "))
num2 = float(input("enter second number: "))

def add(num1, num2):
    addt = num1 + num2
    return addt

def sub(num1, num2):
    subt = num1 - num2
    return subt


print("addition: ", add(num1, num2)) 
print("subtraction: ", sub(num1, num2))


