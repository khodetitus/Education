import re

text_string = """"
www.mongard.ir
www.wikipedia.org
www.realmadrid.com
"""

pattern_url = re.compile(r"(www.)?([\w\-]+\.)?([\w\-]+)\.([\w\-]{2,})(/.*)?", re.MULTILINE)
result = pattern_url.finditer(text_string)
for url in result:
    print(url)
