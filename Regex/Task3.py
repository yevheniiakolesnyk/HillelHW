import re

pattern = re.compile(r'\d{3}.\d{3}.\d{3}')

with open('Data.txt', 'r') as file:
    content = file.read()
    matchers = pattern.findall(content)
    print(matchers)
