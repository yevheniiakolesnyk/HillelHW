course = {'title': 'AQA', 'language': 'Python', 'level': 'PRO', 'frame': 'pytest'}
entered_key = input('Enter any key:')

try:
    ans = course[f'{entered_key}']
except KeyError:
    print(f'"{entered_key}" not found in the dictionary')
else:
    print(ans)
finally:
    print('test is continues')
