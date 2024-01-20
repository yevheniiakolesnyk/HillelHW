list_a = [1, 2, 3, 3, 5, 8, 13, 21, 34, 55, 89]

set_a = set(list_a)

list_b = sorted(list(set_a))

ans = (list_a == list_b)

print(f'Your list is unique: {ans}')

