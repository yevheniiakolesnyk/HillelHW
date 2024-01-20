list_a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
list_b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

set_1 = set(list_a)
set_2 = set(list_b)

ans = set_1.difference(set_2)

print(ans)
