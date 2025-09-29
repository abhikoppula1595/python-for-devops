import sys 


# num1 = 10
# num2 = 5

# def addition():
 #   add = num1 + num2
 #   print(add)

#def sub():
  #  subt = num1 - num2
  #   print(subt)

# def multi():
   #  mul = num1 * num2
    # print(mul)

# def div():
    # divi = num1 / num2
    # print(divi)

# addition()
# sub()
# multi()
# div()



# example 2

def add(num1, num2):
    addt = num1 + num2
    return addt

def sub(num1, num2):
    subt = num1 - num2
    return subt

num1 = float(sys.argv[1])
operation = sys.argv[2]
num2 = float(sys.argv[3])

if operation == "add":
   output = add(num1, num2)
   print(output)

if operation == "sub":
   output = sub(num1, num2)
   print(output)




      