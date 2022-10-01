import re

text_string = """"
11.2.1.2
127.0.0.1
"""

pattern_ip_address = re.compile(r"(\d{1,3})(\.)(\d{1,3})(\.)(\d{1,3})(\.)(\d{1,3})", re.MULTILINE)
result = pattern_ip_address.finditer(text_string)
for ip_address in result:
    print(ip_address)
