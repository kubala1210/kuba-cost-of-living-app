class UserInterface:
    # def __init__(self, country='', city_name='', cost_of_living=0,
    #              cost_of_rent=0, total_cost=0, minimum_salary=0, average_salary=0, r=1, multiplier = 1):
    #     self.country = country
    #     self.city_name = city_name
    #     self.cost_of_living = cost_of_living
    #     self.cost_of_rent = cost_of_rent
    #     self.total_cost = total_cost
    #     self.minimum_salary = minimum_salary
    #     self.average_salary = average_salary
    #     self.multiplier = multiplier
    #     self.r = r
    #     self.history = {}

    def collect_data(self):
        print(
            f'OBLICZENIA MINIMALNEGO WYNAGRODZENIA I WSKAŹNIKA ZAMOŻNOŚCI DLA {(self.__class__.__name__).upper()}')
        self.country = input('Podaj nazwę państwa: ')
        self.city_name = input('Podaj nazwę miasta: ')
        if (any(char.isdigit() for char in self.city_name)
                or any(char.isdigit() for char in self.country)):
            raise TypeError('Nazwa państwa i miasta nie moze zawierać cyfr')
        try:
            self.cost_of_living = float(input(f'Podaj koszty życia dla {self.__class__.__name__} w Twoim mieście: '))
            if self.cost_of_living <= 0:
                raise ValueError(
                    'Koszt życia nie może być mniejszy lub równe 0')
        except Exception as e:
            raise TypeError(f"Błąd: ", e, ' Koszty życia muszą być liczbą.')
        try:
            self.cost_of_rent = float(input('Podaj koszt wynajmu lub kredytu za mieszkanie: '))
            if self.cost_of_rent <= 0:
                raise ValueError(
                    'Koszt wynajmu lub kredytu nie może być mniejszy lub równe 0')
        except Exception as e:
            raise TypeError(f"Błąd: ", e, ' Koszty wynajmu lub kredytu muszą być liczbą.')
        try:
            self.average_salary = float(input('Wprowadź średnie wynagrodzenie w Twoim mieście: '))
            if self.average_salary <= 0:
                raise ValueError(
                    'Średnie wynagrodzenie nie moze być mniejsze lub równe 0')
        except Exception as e:
            raise TypeError('Średnie wynagrodzenie musi być liczbą')

        if self.__class__.__name__ == 'Family2plus1' or self.__class__.__name__ == 'Family2plus2':
            try:
                self.multiplier = float(
                input('Podaj liczbę osób zarabiających w gospodarstwie: '))
            except Exception as e:
                raise TypeError(f"Błąd: ", e, ' Nie podałeś liczby')
        return self.country, self.city_name, self.cost_of_living, self.cost_of_rent, self.average_salary, self.multiplier

    def get_history(self):
        return self.history


class City:

    def __init__(self, data):
        self.city = data.city


    def cost_counter(self):
        self.history[self.__class__.__name__] = {
            'country': self.country,
            'city': self.city_name,
            'cost of living': self.cost_of_living,
            'cost of rent': self.cost_of_rent
        }
        self.cost_of_rent = float(self.cost_of_rent)
        self.total_cost = self.cost_of_living + self.cost_of_rent
        self.history[self.__class__.__name__]['total cost'] = self.total_cost
        print(
            f'Całkowity koszt życia dla {self.__class__.__name__} w {self.country}, {self.city_name} to {self.total_cost}')
        return self.total_cost

    def minimum_salary_counter(self):
        self.minimum_salary = round(((self.total_cost * 1.35) * self.r), 2)
        if self.__class__.__name__ not in self.history:
            self.history[self.__class__.__name__] = {}
        self.history[self.__class__.__name__]['minimum salary'] = self.minimum_salary
        print(
            f'Minimalne wynagrodzenie dla {self.__class__.__name__} w {self.country}, {self.city_name} to: {self.minimum_salary}')
        return self.minimum_salary


class Household(City):

    def wealth_level_counter(self, wealth_level=0, result=''):
        if self.__class__.__name__ not in self.history:
            self.history[self.__class__.__name__] = {}
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
        return wealth_level

    def main_calc(self):
        self.collect_data()
        self.cost_counter()
        self.minimum_salary_counter()
        self.wealth_level_counter()
        self.get_history()