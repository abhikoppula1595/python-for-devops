import re

text = "The quick brown fox"
pattern = r"brown"

search = re.search(pattern, text)
if search:
    print("Pattern found:", search.group())
else:
    print("Pattern not found")

# example 
import re

text = "he is a wonderful person"
pattern = r"abhi"

search = re.search(pattern, text)
if search:
    print("pattern found:", search.group())
else:
    print ("pattern not found")


import re
text = "abhi is in texas"
pattern = r"abhi"

search = re.search(pattern, text)
if search:
    print("pattern found:", search.group())
else:
    print("pattern not found")

    