class City:

    def __init__(self, country='', city_name='', cost_of_living=0,
                 cost_of_rent=0, total_cost=0, minimum_salary=0, average_salary=0):
        self.country = country
        self.city_name = city_name
        self.cost_of_living = cost_of_living
        self.cost_of_rent = cost_of_rent
        self.total_cost = total_cost
        self.minimum_salary = minimum_salary
        self.average_salary = average_salary
        self.history = {}

    def cost_counter(self):
        print(
            f'OBLICZENIA MINIMALNEGO WYNAGRODZENIA I WSKAŹNIKA ZAMOŻNOŚCI DLA {(self.__class__.__name__).upper()}')
        self.country = input('Podaj nazwę państwa: ')
        self.city_name = input('Podaj nazwę miasta: ')
        self.history[self.__class__.__name__] = {
            'country': self.country,
            'city': self.city_name
        }
        if (any(char.isdigit() for char in self.city_name)
                or any(char.isdigit() for char in self.country)):
            raise TypeError('Nazwa państwa i miasta nie moze zawierać cyfr')
        self.cost_of_living = float(
            input(f'Podaj koszty życia dla {self.__class__.__name__} w Twoim mieście: '))
        self.history[self.__class__.__name__]['cost of living'] = self.cost_of_living
        if self.cost_of_living <= 0:
            raise ValueError(
                'Koszty życia nie mogą być rowne lub mniejsze od 0')
        self.cost_of_rent = (
            # jak tutaj zaimplementować raise error w przypadku podania litery zamiast cyfry
            input('Podaj koszt wynajmu lub kredytu za mieszkanie: '))
        self.history[self.__class__.__name__]['cost of rent'] = self.cost_of_rent
        if any(char.isalpha() for char in self.cost_of_rent):
            raise ValueError('Koszt wynajmu lub kredytu nie może zawierać liter')
        self.cost_of_rent = float(self.cost_of_rent)
        if self.cost_of_rent <= 0:
            raise ValueError(
                'Koszty wynajmu lub kredytu nie mogą być równe lub mniejsze od 0')
        self.total_cost = self.cost_of_living + self.cost_of_rent
        self.history[self.__class__.__name__]['total cost'] = self.total_cost
        print(
            f'Całkowity koszt życia dla {self.__class__.__name__} w {self.country}, {self.city_name} to {self.total_cost}')


class Household(City):

    def __init__(self, country='', city_name='', cost_of_living=0,
                 cost_of_rent=0, total_cost=0, minimum_salary=0, average_salary=0, r=1, multiplier=1):
        super().__init__(country, city_name, cost_of_living,
                         cost_of_rent, total_cost, minimum_salary, average_salary)
        self.r = r
        self.multiplier = multiplier

    def minimum_salary_counter(self):
        self.minimum_salary = round(((self.total_cost * 1.35) * self.r), 2)
        self.history[self.__class__.__name__]['minimum salary'] = self.minimum_salary
        print(
            f'Minimalne wynagrodzenie dla {self.__class__.__name__} w {self.country}, {self.city_name} to: {self.minimum_salary}')

    def wealth_level_counter(self, wealth_level=0, result=''):
        self.average_salary = float(
            input('Wprowadź średnie wynagrodzenie w Twoim mieście: '))
        self.history[self.__class__.__name__]['average salary'] = self.average_salary
        if self.average_salary <= 0:
            raise ValueError(
                'Średnie wynagrodzenie nie moze być mniejsze lub równe 0')
        wealth_level = round(
            ((self.average_salary * self.multiplier) / self.minimum_salary), 1)
        self.history[self.__class__.__name__]['wealth level'] = wealth_level
        if wealth_level <= 1:
            result = f'Poziom zamożności {self.__class__.__name__} wynosi {wealth_level}. {self.country}, {self.city_name}, {self.__class__.__name__}  jest mało zamożne'
        elif wealth_level > 1 and wealth_level <= 1.5:
            result = f'Poziom zamożności {self.__class__.__name__} wynosi {wealth_level}. {self.country}, {self.city_name}, {self.__class__.__name__}  jest średnio zamożne'
        elif wealth_level > 1.5 and wealth_level <= 2:
            result = f'Poziom zamożności {self.__class__.__name__} wynosi {wealth_level}. {self.country}, {self.city_name}, {self.__class__.__name__}  jest zamożne'
        elif wealth_level > 2:
            result = f'Poziom zamożności {self.__class__.__name__} wynosi {wealth_level}. {self.country}, {self.city_name}, {self.__class__.__name__}  jest bardzo zamożne'
        self.history[self.__class__.__name__]['wealth description'] = result
        print(result)

    def get_history(self):
        print(self.history)

# PONIŻSZE KLASY WEDŁUG MNIE POWINNY BYĆ USUNIĘTE, PONIEWAŻ POWTARZAJĄ SIĘ W calculator.py
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
        self.multiplier = float(
            input('Podaj liczbę osób zarabiających w gospodarstwie: '))
        if self.multiplier <= 0:
            raise ValueError('Liczba osób nie może być mniejsza lub równa 0')
        super().wealth_level_counter()


class Family2plus2(Household):

    def minimum_salary_counter(self):
        self.r = 3.5
        super().minimum_salary_counter()

    def wealth_level_counter(self, wealth_level=0, result=''):
        self.multiplier = float(
            input('Podaj liczbę osób zarabiających w gospodarstwie: '))
        if self.multiplier <= 0:
            raise ValueError('Liczba osób nie może być mniejsza lub równa 0')
        super().wealth_level_counter()


# PONIŻSZE TYLKO DO SPRAWDZANIA DZIAŁANIA MODUŁU HOUSEHOLDS
if __name__ == '__main__':
    single_01 = Single()
    couple_01 = Couple()
    family_01 = Family2plus1()
    family_02 = Family2plus2()
    single_01.get_history()
    single_01.cost_counter()
    single_01.minimum_salary_counter()
    single_01.wealth_level_counter()
    single_01.get_history()

