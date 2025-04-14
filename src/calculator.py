class UserInterface:

    def collect_data(self, multiplier=1):
        family_type = input(
            'Podaj rodzaj gospodarstwa domowego single/couple/family2plus1/family2plus2: ').upper()
        country = input(
            'Podaj nazwę państwa: ')
        city_name = input(
            'Podaj nazwę miasta: ')
        cost_of_living = float(input(
            f'Podaj koszty życia dla {family_type} w Twoim mieście: '))
        cost_of_rent = float(input(
            'Podaj koszt wynajmu lub kredytu za mieszkanie: '))
        average_salary = float(input(
            'Wprowadź średnie wynagrodzenie w Twoim mieście: '))
        if family_type == 'Family2plus1' or family_type == 'Family2plus2':
            multiplier = float(input(
                'Podaj liczbę osób zarabiających w gospodarstwie: '))
        return family_type, country, city_name, cost_of_living, cost_of_rent, average_salary, multiplier


class City:

    def __init__(self, validated_data):
        self.family_type = validated_data.family_type
        self.country = validated_data.country
        self.city_name = validated_data.city_name
        self.cost_of_living = validated_data.cost_of_living
        self.cost_of_rent = validated_data.cost_of_rent
        self.average_salary = validated_data.average_salary
        self.multiplier = validated_data.multiplier

    def cost_counter(self):
        print(
            f'OBLICZENIA MINIMALNEGO WYNAGRODZENIA I WSKAŹNIKA ZAMOŻNOŚCI DLA {(self.family_type).upper()}')
        self.cost_of_rent = float(self.cost_of_rent)
        total_cost = self.cost_of_living + self.cost_of_rent
        print(
            f'Całkowity koszt życia dla {self.family_type} w {self.country}, {self.city_name} to {total_cost}')
        return total_cost

    def minimum_salary_counter(self, total_cost):
        if self.family_type == 'SINGLE':
            r = 1
        elif self.family_type == 'COUPLE':
            r = 1.9
        elif self.family_type == 'FAMILY2PLUS1':
            r = 2.7
        elif self.family_type == 'FAMILY2PLUS2':
            r = 3.5
        minimum_salary = round(((total_cost * 1.35) * r), 2)
        print(
            f'Minimalne wynagrodzenie dla {self.family_type} w {self.country}, {self.city_name} to: {minimum_salary}')
        return minimum_salary


class Household(City):

    def wealth_level_counter(self, minimum_salary):
        wealth_level = round(
            ((self.average_salary * self.multiplier) / minimum_salary), 1)
        return wealth_level

    def display_wealth_level(self, wealth_level):
        if wealth_level <= 1:
            result = f'Poziom zamożności {self.family_type} wynosi {wealth_level}. {self.country}, {self.city_name}, {self.family_type}  jest mało zamożne'
        elif wealth_level > 1 and wealth_level <= 1.5:
            result = f'Poziom zamożności {self.family_type} wynosi {wealth_level}. {self.country}, {self.city_name}, {self.family_type}  jest średnio zamożne'
        elif wealth_level > 1.5 and wealth_level <= 2:
            result = f'Poziom zamożności {self.family_type} wynosi {wealth_level}. {self.country}, {self.city_name}, {self.family_type}  jest zamożne'
        elif wealth_level > 2:
            result = f'Poziom zamożności {self.family_type} wynosi {wealth_level}. {self.country}, {self.city_name}, {self.family_type}  jest bardzo zamożne'
        return result


class History:

    def __init__(self):
        self.calc_history = {}
        self.error_history = {}

    def save_calc_data(self, family_type='', country='', city_name='', cost_of_living=1, cost_of_rent=1,
                       average_salary=1, minimum_salary=1, total_cost=1, wealth_level=1):
        if country not in self.calc_history:
            self.calc_history[country] = {}
        if city_name not in self.calc_history[country]:
            self.calc_history[country][city_name] = {
                'cost of living': cost_of_living,
                'cost of rent': cost_of_rent,
                'average salary': average_salary,
                'minimum salary': minimum_salary,
                'total cost': total_cost,
                'wealth level': wealth_level
            }

    def save_error_history(self, error=''):
        if 'Errors' not in self.error_history:
            self.error_history['Errors'] = []
        self.error_history['Errors'].append(str(error))
