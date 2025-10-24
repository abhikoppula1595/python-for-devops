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



