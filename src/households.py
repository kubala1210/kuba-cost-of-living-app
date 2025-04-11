from calculator import Household

# MYŚLĘ, ŻE W ZWIĄZKU ZE ZMIANAMI TEGO MODUŁU MOŻNA SIĘ CAŁKIEM POZBYĆ -
# CHYBA, ŻE BĘDZIE MIAŁ SPEŁNIAĆ INNĄ FUNKCJĘ


class Single(Household):
    pass


class Couple(Household):

    def minimum_salary_counter(self):
        self.r = 1.9
        super().minimum_salary_counter()

    def wealth_level_counter(self, wealth_level=0, result=''):
        self.multiplier = 2
        super().wealth_level_counter()


class Family2plus1(Household):

    def minimum_salary_counter(self):
        self.r = 2.7
        super().minimum_salary_counter()

    def wealth_level_counter(self, wealth_level=0, result=''):
        if self.multiplier <= 0:
            raise ValueError('Liczba osób nie może być mniejsza lub równa 0')
        super().wealth_level_counter()


class Family2plus2(Household):

    def minimum_salary_counter(self):
        self.r = 3.5
        super().minimum_salary_counter()

    def wealth_level_counter(self, wealth_level=0, result=''):
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
        family_01.main_calc()
        family_02.main_calc()
    except Exception as error:
        print(error)
        raise








# PONIŻSZE KLASY WEDŁUG MNIE POWINNY BYĆ USUNIĘTE, PONIEWAŻ POWTARZAJĄ SIĘ W calculator.py
# class Single(Household):
#     pass
#
#
# class Couple(Household):
#
#     def minimum_salary_counter(self):
#         self.r = 1.9
#         super().minimum_salary_counter()
#
#     def wealth_level_counter(self, wealth_level=0, result=''):
#         self.multiplier = 2
#         super().wealth_level_counter()
#
#
# class Family2plus1(Household):
#
#     def minimum_salary_counter(self):
#         self.r = 2.7
#         super().minimum_salary_counter()
#
#     def wealth_level_counter(self, wealth_level=0, result=''):
#         if self.multiplier <= 0:
#             raise ValueError('Liczba osób nie może być mniejsza lub równa 0')
#         super().wealth_level_counter()
#
#
# class Family2plus2(Household):
#
#     def minimum_salary_counter(self):
#         self.r = 3.5
#         super().minimum_salary_counter()
#
#     def wealth_level_counter(self, wealth_level=0, result=''):
#         self.multiplier = float(
#             input('Podaj liczbę osób zarabiających w gospodarstwie: '))
#         if self.multiplier <= 0:
#             raise ValueError('Liczba osób nie może być mniejsza lub równa 0')
#         super().wealth_level_counter()


# PONIŻSZE TYLKO DO SPRAWDZANIA DZIAŁANIA MODUŁU HOUSEHOLDS
# if __name__ == '__main__':
#     single_01 = Single()
#     couple_01 = Couple()
#     family_01 = Family2plus1()
#     family_02 = Family2plus2()
#     single_01.collect_data()
#     single_01.get_history()
#     single_01.cost_counter()
#     single_01.minimum_salary_counter()
#     single_01.wealth_level_counter()
#     single_01.get_history()

