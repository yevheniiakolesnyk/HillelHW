class CafeEmployee:
    list_positions = []

    def __init__(self, name, position, month_best_employee='No'):
        self.name = name
        self.position = position
        self.month_best_employee = month_best_employee
        CafeEmployee.list_my(name, position)

    def congratulations(self):
        if self.month_best_employee == 'Yes':
            print(f'{self.name}, you\'re the best {self.position} of the month! Congrats!')
        else: print(f'{self.name}, we\'ll recall you')

    @staticmethod
    def working_hours(days_in_month):
        result = (days_in_month -8) * 8
        return result

    @classmethod
    def list_my(cls, name, position):
        cls.list_positions.append(position)
        return cls.list_positions


Lora = CafeEmployee('Lora', 'Waiter')
Olga = CafeEmployee('Olga', 'Waiter', 'Yes')
Nora = CafeEmployee('Nora', 'Administrator', 'Never')
print(CafeEmployee.list_positions)
Olga.congratulations()
Lora.congratulations()
Nora.congratulations()
work_hours_per_month = CafeEmployee.working_hours(30)
print(work_hours_per_month)
