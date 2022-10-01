import re

text_string = """"
1922-02-02
1340/02/01
"""

pattern_date = re.compile(r"(\d{4})[.\-/](\d{2})[.\-/](\d{2})", re.MULTILINE)
result = pattern_date.finditer(text_string)
for date in result:
    print(date)
