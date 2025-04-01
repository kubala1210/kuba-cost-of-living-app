from households import Household

class CostCalculator(Household):

    def __init__(self, country='', city_name='', cost_of_living=0, cost_of_rent=0, total_cost=0,
                 minimum_salary=0, average_salary=0, family_type='', r=1):
        super().__init__(country, city_name, cost_of_living, cost_of_rent, total_cost,
                         minimum_salary, average_salary, family_type, r)

    def main_calc(self):
        self.cost_counter()
        self.minimum_salary_counter()
        print(self.wealth_level_counter())


household_1 = CostCalculator()
household_1.main_calc()

