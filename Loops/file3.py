# Solution 1
number = 1

while number <= 4:
    print('*' * number)
    number += 1


# Solution 2
x = 0
y = -1

while x < 4:
    while y < 0:
        print('*', end= '')
        y = y + 1
    print()
    x = x + 1
    y = y - 2
