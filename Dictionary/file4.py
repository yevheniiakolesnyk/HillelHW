result_link = 'https://www.youtube.com/watch?v=some_id&list=some_list&index=6&t=0s'

elements_dict = {}

for elements in result_link:
    if elements in elements_dict:
        elements_dict[elements] += 1
    else:
        elements_dict[elements] = 1

print(elements_dict)

