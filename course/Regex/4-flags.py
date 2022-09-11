import re

text_string = """hellow world 
h6llo nice H7LLO
"""

pattern = re.compile("h.llo", re.IGNORECASE)
# pattern = re.compile("h.llo", re.LOCALE)
# pattern = re.compile("h.llo", re.MULTILINE)
# pattern = re.compile("h.llo", re.DOTALL)
# pattern = re.compile("h.llo", re.ASCII)
# pattern = re.compile("h.llo", re.VERBOSE)
# pattern = re.compile("h.llo", re.IGNORECASE | re.MULTILINE)
result = pattern.findall(text_string)
print(result)
