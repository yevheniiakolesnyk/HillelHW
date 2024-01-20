def square():
    for numbers in range(0, 1000000001, 2):
        yield numbers**2

ans = square()
print(next(ans))
print(next(ans))
print(next(ans))