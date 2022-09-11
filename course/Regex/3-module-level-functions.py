# using regex with module-level functions
import re

print(re.match(r"h.llo", "hello world h6llo nice h7llo"))
print(re.search(r"h.llo", "hello world h6llo nice h7llo"))
print(re.findall(r"h.llo", "hello world h6llo nice h7llo"))
print(re.finditer(r"h.llo", "hello world h6llo nice h7llo"))
