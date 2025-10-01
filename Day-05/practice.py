# arithmetic operators
print("arithmetic")

a = 10
b = 5

add = a + b
sub = a - b
mul = a * b
div = a / b
reminder = a % b
float = a // b

print("addition:", add)
print("subtract:", sub)
print("product:", mul)
print("quotient:", div)


print("comparison")

a = 50
b = 20

print(a < b)
print(a > b)
print(a <= b)
print(a >=b)
print(a == b)
print(a != b)

print("logical")

print(" ")

x = 10
y = 20

print("and statements")
print(x != y and x < y)
print(x == y and x > y)
print(x < y and x == y)
print(x >= y and x <= y)

print("or statements")
print(x != y or x < y)
print(x == y or x > y)
print(x < y or x == y)
print(x >= y or x <= y)


print("not statement")
print(not(x == y))
print(not(x < y))
print(not(x != y))

print("assignment")
print(" ")

print()

#################

x = 20

x += 10
x -= 10
x /= 10
x *= 10

print("final value:", x)


##################
print(" ")



my_list = [1, 2, 3, 4, 5]

# Identity operators
a = my_list
b = [1, 2, 3, 4, 5]

is_same_object = a is my_list
is_not_same_object = b is not my_list

# Membership operators
element_in_list = 3 in my_list
element_not_in_list = 6 not in my_list

print("a is my_list:", is_same_object)
print("b is not my_list:", is_not_same_object)
print("3 in my_list:", element_in_list)
print("6 not in my_list:", element_not_in_list)

