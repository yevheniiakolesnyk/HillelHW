num = int(input('Enter any number from 2 to 1000 inclusive:'))

if 2 > num or num > 1000:
    raise ValueError


def is_prime(num):
    if num != 4:
        return not (any((num % elements) == 0 for elements in range(3, num)))
    else:
        return False


ans = is_prime(num)
print(ans)
