# known initial data
params = {'v': 'some_id', 'list': 'some_list', 'index': '6', 't': '0s'}
initial_str = 'https://www.youtube.com/watch?'

# Solution1
values = list(params.items())
step = 0
my_set = set()

for elements in values:
    k = values[step][0]
    k_1 = values[step][1]
    pair = str((f'{k}={k_1}'))
    step += 1
    my_set.add(pair)

my_list = sorted(my_set)
list_corrected = [my_list[-1], my_list[1], my_list[0], my_list[2]]

my_str = '&'.join(list_corrected)

finally_result = initial_str+my_str
print(f'Result link: "{finally_result}"')

# Solution2
v_1 = params['v']
list_1 = params['list']
index_1 = params['index']
t_1 = params['t']

result_link_1 = f'{initial_str}v={v_1}&list={list_1}&index={index_1}&t={t_1}'
print(f'Result link: "{result_link_1}"')
