# using regex with pre-compile
import re  # first import library

text_string = "hello world h6llo nice h7llo"  # second make a text choose
pattern = re.compile(r"h.llo")  # third make a pattern regex for text
result = pattern.match(text_string)  # fourth we change our object to the desired method
# result = pattern.search(text_string)
# result = pattern.findall(text_string)
# result = pattern.finditer(text_string)
# for match_string in result:
#     print(match_string)
print(result)  # fifth print the object match

# output:
# <re.Match object; span=(0, 5), match='hello'>
# span:range index
# match:match the string text with pattern

# note:
# name = "Masoud"  # string variable = string literal
