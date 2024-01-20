num_1 = int(input('Enter any number:'))
num_2 = int(input('Enter another number:'))
operation = input('Enter required operation (allowed:+, -, *, /):')


def math_feature(num_1, num_2, operation):
    if operation == '+':
        return num_1 + num_2
    elif operation == '-':
        return num_1 - num_2
    elif operation == '*':
        return num_1 * num_2
    elif operation == '/':
        return int(num_1 / num_2)
    else:
        print(f'Not known operation "{operation}"')


ans = math_feature(num_1, num_2, operation)
print(ans)

