
for i in range (20):
    print("abhi")
    print("koppula")
    print(i)


#################
colours = ["red", "blue", "black"]
for x in range(3):
    print(colours)

#############
print(" ")
######################
#while loop

number = 5
while number <= 5:
    print(number)
    number = number + 1

###########################

battery = 60

while battery > 10:
    print("phone is good to use", battery)

    battery -= 5
    battery -= 50
    battery += 10
    battery -= 10



print("battery low about to shutdown")


#####################
numbers = [1, 2, 3, 4, 5]

for x in numbers:
    if x == 3:
     break
    print(x)

######################

numbers = [1, 2, 3, 4, 5]

for x in numbers:
    if x == 3:
     continue
    print(x)