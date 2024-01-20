class Animals:

    def __init__(self, name: str, place_living: str, population: int, program_name: str):
        self.name = name
        self._place_living = place_living
        self.__population = population
        self._program_name = program_name

    def __repr__(self):
        return f'{self.name} live in {self.place_living} in population of {self.__population}'

    @property
    def place_living(self):
        return self._place_living

    @property
    def program_name(self):
        return self._program_name

    @program_name.setter
    def program_name(self, new_name_program: str):
        if not new_name_program.isalpha():
            raise ValueError('Set string')
        else:
            self._program_name = new_name_program

    def target_year_population(self, increment_per_year):
        if increment_per_year < 200:
            raise ValueError('Pay attention to the population')
        return (self.__population + increment_per_year) / 100

    def get_place_living(self, place: str):
        if place == 'box':
            raise PermissionError('You have no permissions to use this class')
        else:
            return self.__population


birds = Animals('Calibri', 'Savanna', 1000, 'Save animals')
print(birds)
print(birds.target_year_population(250))
print(birds.get_place_living('box1'))
print(birds.place_living)
birds.program_name = 'Wood'
print(birds.program_name)
