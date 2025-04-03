from households import Household


class CostCalculator(Household):

    def main_calc(self):
        self.cost_counter()
        self.minimum_salary_counter()
        self.wealth_level_counter()


class Single(CostCalculator):
    pass


class Couple(CostCalculator):

    def minimum_salary_counter(self):
        self.r = 1.9
        super().minimum_salary_counter()

    def wealth_level_counter(self, wealth_level=0, result=''):
        self.multiplier = 2
        super().wealth_level_counter()


class Family2plus1(CostCalculator):

    def minimum_salary_counter(self):
        self.r = 2.7
        super().minimum_salary_counter()

    def wealth_level_counter(self, wealth_level=0, result=''):
        self.multiplier = float(
            input('Podaj liczbę osób zarabiających w gospodarstwie: '))
        if self.multiplier <= 0:
            raise ValueError('Liczba osób nie może być mniejsza lub równa 0')
        super().wealth_level_counter()


class Family2plus2(CostCalculator):

    def minimum_salary_counter(self):
        self.r = 3.5
        super().minimum_salary_counter()

    def wealth_level_counter(self, wealth_level=0, result=''):
        self.multiplier = float(
            input('Podaj liczbę osób zarabiających w gospodarstwie: '))
        if self.multiplier <= 0:
            raise ValueError('Liczba osób nie może być mniejsza lub równa 0')
        super().wealth_level_counter()


# PONIŻSZE TYLKO DO SPRAWDZANIA DZIAŁANIA MODUŁU
if __name__ == '__main__':
    try:
        single_01 = Single()
        couple_01 = Couple()
        family_01 = Family2plus1()
        family_02 = Family2plus2()

        single_01.main_calc()
        couple_01.main_calc()
        amily_01.main_calc()
        family_02.main_calc()
    except Exception as error:
        print(error)
        raise
