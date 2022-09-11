import re

text_string = """
#99ff44
#5d7
#e28cc2
"""

pattern_hex1 = re.compile(r"^#(\w{6}|\w{3}$)", re.MULTILINE)
pattern_hex2 = re.compile(r"^#(\w{0,6})", re.MULTILINE)
pattern_hex3 = re.compile(r"^#(\w)", re.MULTILINE)
result = pattern_hex1.finditer(text_string)
for tags in result:
    print(tags)
