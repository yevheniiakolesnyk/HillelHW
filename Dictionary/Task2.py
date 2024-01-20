roles = {'admin': ['Olga', 'Lena'],
          'maintainer': ['Igor', 'Sasha'],
          'manager': ['Ira', 'Natasha'],
          'developer': ['Lora', 'Peter']
          }

user_request = input('Please, enter your name:')
step = 0
available_names = list(roles.values())

for my_keys, my_names in roles.items():
    if user_request.strip() in my_names:
       print(f'Hello {my_keys}')
       break
    else: step +=1
    if step == 3:
        print('Hello Guest')
