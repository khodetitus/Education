import re

text_string = """"
example@email.co
exampleemail.co
akbar
asd @ gmail.com
akbar.babaii@yahoo.com
"""

pattern_email = re.compile(r"^([\w\-.]+)@([\w\-]+)\.([a-zA-Z]{2,5})$", re.MULTILINE)
result = pattern_email.finditer(text_string)
for email in result:
    print(email)
