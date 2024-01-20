my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 12]

for number in my_list:
    ind = my_list.index(number)
    x = (number-1 == ind)
    if x is False:
        print(number)
        break
else: print('Your list is fine')

