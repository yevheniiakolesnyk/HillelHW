from Hw15.Animals import Animals


class Mammals(Animals):

    def __init__(self, name: str, place_living: str, population: int, program_name: str) -> object:
        super().__init__(name, place_living, population, program_name)
        self._meal = 'Mushrooms'

    def program_name(self):
        return self._program_name

    def eating(self):
        print(f'{self._meal} is usual meal for {self.name}')

    def required_eating(self, per_day_days: int, period: int):
        meal_to_eat = per_day_days * period
        return f'{self.name} requires {meal_to_eat} killo of food'

    def get_eat(self):
        if self.name == 'Lagomorpha':
            return self._meal
        else:
            return 'Only langomorpha eat a secret meal'


lagomorpha = Mammals('Lagomorpha', 'Forest', 1500, 'Save Mammals')
print(lagomorpha)
print(lagomorpha.required_eating(10, 2))
print(lagomorpha.get_eat())
