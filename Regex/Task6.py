import re

pattern = re.compile(r'\w+@\w+\.\w+')

with open('Data.txt', 'r') as file:
    content = file.read()
    matchers = pattern.findall(content)
    print(matchers)
