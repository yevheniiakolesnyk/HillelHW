from collections import namedtuple

forest = namedtuple('forest', ['trees', 'animals', 'population'])

forest_1 = forest('spruce', 'bear', 1000)
forest_2 = forest('pine', 'wolf', 1200)
forest_3 = forest(1_000_000, 'boar', 400)

forests = [forest_1, forest_2, forest_3]

for frs in forests:
    if type(frs.trees) != str:
        print(f'Warning! Invalid data type. Expected result is str, Actual is {type(frs.trees)}')
        continue
    if type(frs.animals) != str:
        print(f'Warning! Invalid data type. Expected result is str, Actual is {type(frs.trees)}')
        continue
    if type(frs.population) != int:
        print(f'Warning! Invalid data type. Expected result is int, Actual is {type(frs.trees)}')
    else:
        print(f'In your forest are {frs.trees} trees with living there {frs.animals}. Just imagine, there\'re {frs.population} animals now')
