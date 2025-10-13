#in-built functions practice

str1 = "abhi"
str2 = "koppula"

result = str1 + " " + str2
print(result)

#example_2_length

text = "my name is abhi"
result = len(text)

print(result)

text2 = "in this world"
print(len(text2))

print(" ")

#example_3

name = "ABHI koppula"
lowercase = name.lower()
uppercase = name.upper()

print(lowercase)
print(uppercase)

print(" ")

#example_4

text = "abhi is a strong person"
replace = text.replace("strong" , "successful")
print(replace)

print(" ")

#EXAMPLE_5

text = "mynameis/abhi"
word = text.split("/")
print(word)
print(" ")

#example-6- remove unneccessary gaps end of string
text = "abhi is in texas    "
new = text.strip()
print(new)
print(" ")

#substring

text = "india always my country"
substring = "is"
if substring in text:
    print(substring, "found in text")
else:
    print("not found")

fruits = ["apple", "banana", "cherry"]
print("banana" in fruits) 
print("mango" in fruits) 

print(" ")

#float

x = 2.4
y = 2.9
value = x + y
print(value)

num3 = 3.5
num4 = 1.22

result1 = num3 + num4
print("addition:", result1)

result2 = num3 - num4
print("subtraction:", result2)

result3 = num3 * num4
print("multiplication:", result3)

result4 = num3 / num4
print("division:", result4)

result5 = round(1.123456, 3)
print("rounded:", result5)
print(" ")

#####
#regex-findall

import re

text = "the quick brown fox"
pattern = r"brown"

search = re.search(pattern, text)
if search:
    print("pattern found:", search.group())
else:
    print("pattern not found")


#findall
import re
text = " indian army is strongest army"
pattern = r"army"
search = re.findall(pattern , text)
if search:
    print("pattern found:", search)
else:
    print("pattern not found")

#match
import re
text = " indian army is strongest"
pattern = r"army"
search = re.match(pattern , text)
if search:
    print("pattern found:", search.group())
else:
    print("pattern not found")

import re

text = "The quick brown fox"
pattern = r"quick"

match = re.match(pattern, text)
if match:
    print("Match found:", match.group())
else:
    print("No match")


import re

text = "the devops job"
pattern ="the"

match = re.match(pattern, text)
if match:
    print("match found:", match.group())
else:
    print("match not found")

print(" ")

#replace

text = "abhi is very good"
word = r"good"

replace = "awesome"

new_word = re.sub(word, replace, text)
print(new_word)

#split

import re
text = "apple,orange,grapes"
pattern = r","

split_result = re.split(pattern, text)
print(split_result)