import re

text = "Contact me at sample123@gmail.com or 9876543210"

email = re.search(r'\w+@\w+\.\w+', text)
number = re.search(r'\d{10}', text)

print("Email:", email.group())
print("Number:", number.group())