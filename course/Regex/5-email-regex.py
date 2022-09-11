import re

text_string = """"
masoudpro2@gmail.com
nice23@gmail.com
good.bad@yahoo.com
masoudzandi.binancepro2@gmail.com
"""

pattern_email = re.compile(r"^([\w\-.]+)@([\w\-]+)\.([a-zA-Z]{2,5})$", re.MULTILINE)
result = pattern_email.finditer(text_string)
for email in result:
    print(email)
