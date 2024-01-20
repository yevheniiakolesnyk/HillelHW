family = {
  'grandpa': ('Alex', 76),
  'grandma': ('Nona', 74),
  'dad': ('Greg', 48),
  'mom': ('July', 45),
  'son_older': ('Bob', 18),
  'son_middle': ('Alex', 15),
  'son_young': ('Mark', 10)
}

age_list = list(family.values())

max_age = age_list[0][-1]
my_set_max = set()
step = 0

for elements_max in age_list:
    max_numbers = age_list[step][-1]
    step += 1
    if max_numbers >= max_age:
        my_set_max.add(max_numbers)

min_age = age_list[0][-1]
my_set_min = set()
step = 0

for elements_min in age_list:
    min_numbers = age_list[step][-1]
    step += 1
    if min_numbers <= min_age:
        my_set_min.add(min_numbers)

answer = (max(my_set_max) - min(my_set_min))
print(f'The difference is: {answer}')
