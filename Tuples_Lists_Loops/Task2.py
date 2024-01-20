message = '1 2 3 You received 3 new 3 mo 1 my no mo'
message_list = message.split(' ')
my_count = 0

for element in message_list:
    if element.isalpha():
        my_count += 1
        if my_count == 3:
            print(f'Your message "{message}" has 3 words one by one')
            break
    else: my_count = 0
if my_count !=3:
    print(f'Your message "{message}" doesn\'t have 3 words one by one')
