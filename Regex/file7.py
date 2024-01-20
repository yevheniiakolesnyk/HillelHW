import re
from Regex.Examples import urls

pattern = re.compile(r'https?://(www\.)?(\w+)(\.\w+)')

matchers = pattern.finditer(urls)
for elements in matchers:
    print(elements.group())

subbed_str = re.sub(r'https?://(www\.)?(\w+)(\.\w+)',r'\2\3', urls)
print(subbed_str)
