import re

text = "The quick brown fox jumps over the lazy brown dog"
pattern = r"brown"

replacement = "red"

new_text = re.sub(pattern, replacement, text)
print("Modified text:", new_text)


import re

text = "india is a great i love india"
pattern = r"india"

replacement = "hyderabad"

new_text = re.sub(pattern, replacement, text)
print("modified text:", new_text)


