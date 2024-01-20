my_list = [2, 5, 1, 6, 9, 22, 21, 32, 90]
division_number = float(input('Enter some number:'))

for number in my_list:
    if number % division_number == 0:
        print(number)

