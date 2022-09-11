import re

# 1:

text_string = "hello world"
pattern = re.compile(r"h.llo")
result = pattern.match(text_string)
print(f"range index: {result.span()}")
print(f"start index :{result.start()}")
print(f"end index : {result.end()}")
print(f"match string with pattern : {result.group()}")

# 2:

text = "abcabcabc"
p = re.compile(r"a")
result1 = p.split(text)
result2 = p.sub("N", text)
result3 = p.subn("N", text)
print(result1)
print(result2)
print(result3)
