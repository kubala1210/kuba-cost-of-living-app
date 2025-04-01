from households import Household

class CostCalculator(Household):

    def main_calc(self):
        self.cost_counter()
        self.minimum_salary_counter()
        self.wealth_level_counter()

class Single(CostCalculator):

    def cost_counter(self):
        print('Obliczenia minimalnego wynagrodzenia oraz wskaźnika zamożności dla singla')
        super().cost_counter()

    def minimum_salary_counter(self):
        super().minimum_salary_counter()
        print(f'Minimalne wynagrodzenie dla singla to: {self.minimum_salary}')

    def wealth_level_counter(self, wealth_level=0, result=''):
        self.multiplier = 1
        super().wealth_level_counter()
        print(result)

class Couple(CostCalculator):

    def cost_counter(self):
        print('Obliczenia minimalnego wynagrodzenia oraz wskaźnika zamożności dla pary')
        super().cost_counter()

    def minimum_salary_counter(self):
        super().minimum_salary_counter()
        print(f'Minimalne wynagrodzenie dla pary to: {self.minimum_salary}')

    def wealth_level_counter(self, wealth_level=0, result=''):
        self.multiplier = 2
        super().wealth_level_counter()
        print(result)

class Family2plus1(CostCalculator):

    def cost_counter(self):
        print('Obliczenia minimalnego wynagrodzenia oraz wskaźnika zamożności dla rodziny 2+1')
        super().cost_counter()

    def minimum_salary_counter(self):
        super().minimum_salary_counter()
        print(f'Minimalne wynagrodzenie dla rodziny 2+1 to: {self.minimum_salary}')

    def wealth_level_counter(self, wealth_level=0, result=''):
        self.multiplier = float(input('Podaj liczbę osób zarabiających w gospodarstwie: '))
        super().wealth_level_counter()
        print(result)

class Family2plus2(CostCalculator):

    def cost_counter(self):
        print('Obliczenia minimalnego wynagrodzenia oraz wskaźnika zamożności dla rodziny 2+2')
        super().cost_counter()

    def minimum_salary_counter(self):
        super().minimum_salary_counter()
        print(f'Minimalne wynagrodzenie dla rodziny 2+2 to: {self.minimum_salary}')

    def wealth_level_counter(self, wealth_level=0, result=''):
        self.multiplier = float(input('Podaj liczbę osób zarabiających w gospodarstwie: '))
        super().wealth_level_counter()
        print(result)

single_01 = Single()
couple_01 = Couple()
family_01 = Family2plus1()
family_02 = Family2plus2()

single_01.main_calc()
couple_01.main_calc()
family_01.main_calc()
family_02.main_calc()
