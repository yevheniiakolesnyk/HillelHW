import re
from Hw13.Examples import text_to_search

pattern = re.compile(r'abc')

matchers = pattern.finditer(text_to_search)

for items in matchers:
    print(items)

print(text_to_search[1:4])
