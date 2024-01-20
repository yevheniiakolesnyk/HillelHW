from Classes.Mammals import Mammals


class Predators(Mammals):

    def __init__(self, name: str, place_living: str, population: int, program_name: str) -> object:
        super().__init__(name, place_living, population, program_name)
        self.new_population = 200


    def __repr__(self):
        return f'{self.name} belongs to predators'

    def target_year_population(self, increment_per_year):
        if increment_per_year > 200:
            print('There\'s a great population raise!')
        return (self.new_population + increment_per_year) / 100

    def _target_population_per_month(self):
        targ = self.new_population / 12
        return targ

    def schedule_slippage(self, pessimistic_population):
        return self._target_population_per_month() - pessimistic_population



tiger = Predators('tiger', 'pride', 210, 'Save predators')
print(tiger.target_year_population(101))
print(tiger)
print(tiger.schedule_slippage(3))
