import re
from Regex.Examples import text_to_search

pattern = re.compile(r'\d{3}[*-]\d{3}[*-]\d{3,4}')

matchers = pattern.findall(text_to_search)
print(matchers)
