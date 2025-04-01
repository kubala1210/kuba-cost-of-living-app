class City:

    def __init__(self, country, city_name, cost_of_living=0,
                 cost_of_rent=0, total_cost=0, minimum_salary=0, average_salary=0):
        self.country = country
        self.city_name = city_name
        self.cost_of_living = cost_of_living
        self.cost_of_rent = cost_of_rent
        self.total_cost = total_cost
        self.minimum_salary = minimum_salary
        self.average_salary = average_salary

    def cost_counter(self):
        self.cost_of_living = float(input('Podaj koszty życia w Twoim mieście: '))
        self.cost_of_rent = float(input('Podaj koszt wynajmu lub kredytu za mieszkanie: '))
        self.total_cost = self.cost_of_living + self.cost_of_rent
        print(f'Całkowity koszt życia w Twoim gospodarstwie domowym to {self.total_cost}')

class Household(City):

    def __init__(self, country, city_name, cost_of_living=0,
                 cost_of_rent=0, total_cost=0, minimum_salary=0, average_salary=0, family_type='', r=1):
        super().__init__(country, city_name, cost_of_living, cost_of_rent, total_cost, minimum_salary, average_salary)
        self.family_type = family_type
        self.r = r

    def minimum_salary_counter(self):
        self.family_type = input('Podaj rodzaj gospodarstwa domowego singiel/para/2+1/2+2: ')
        if self.family_type == 'singiel':
            self.r = 1
        if self.family_type == 'para':
            self.r = 1.9
        if self.family_type == '2+1':
            self.r = 2.7
        if self.family_type == '2+2':
            self.r = 3.5
        self.minimum_salary = (self.total_cost * 1.35) * self.r
        return f'Minimalne wynagrodzenie to: {self.minimum_salary}'

    def wealth_level_counter(self, wealth_level=0):
        if not self.family_type == 'singiel':
            multiplier = 2
        self.average_salary = float(input('Wprowadź średnie wynagrodzenie w Twoim mieście: '))
        wealth_level = round(((self.average_salary * multiplier) / self.minimum_salary), 1)
        if wealth_level <= 1:
            return f'Poziom zamożności wynosi {wealth_level}. Społeczeństwo jest mało zamożne'
        if wealth_level > 1 and wealth_level <= 1.5:
            return f'Poziom zamożności wynosi {wealth_level}. Społeczeństwo jest średnio zamożne'
        if wealth_level > 1.5 and wealth_level <= 2:
            return f'Poziom zamożności wynosi {wealth_level}. Społeczeństwo jest zamożne'
        if wealth_level > 2:
            return f'Poziom zamożności wynosi {wealth_level}. Społeczeństwo jest bardzo zamożne'

class Single(Household):

    def __init__(self, country, city_name, cost_of_living=0,
                 cost_of_rent=0, total_cost=0, minimum_salary=0, average_salary=0, family_type='', r=1):
        super().__init__(country, city_name, cost_of_living, cost_of_rent, total_cost,
                         minimum_salary, average_salary, family_type, r)

    def minimum_salary_counter(self):
        self.family_type = input('Podaj rodzaj gospodarstwa domowego singiel/para/2+1/2+2: ')
        if self.family_type == 'singiel':
            self.r = 1
        if self.family_type == 'para':
            self.r = 1.9
        if self.family_type == '2+1':
            self.r = 2.7
        if self.family_type == '2+2':
            self.r = 3.5
        self.minimum_salary = (self.total_cost * 1.35) * self.r
        return f'Minimalne wynagrodzenie to: {self.minimum_salary}'

    def wealth_level_counter(self, wealth_level=0):
        if not self.family_type == 'singiel':
            multiplier = 2
        self.average_salary = float(input('Wprowadź średnie wynagrodzenie w Twoim mieście: '))
        wealth_level = round(((self.average_salary * multiplier) / self.minimum_salary), 1)
        if wealth_level <= 1:
            return f'Poziom zamożności wynosi {wealth_level}. Społeczeństwo jest mało zamożne'
        if wealth_level > 1 and wealth_level <= 1.5:
            return f'Poziom zamożności wynosi {wealth_level}. Społeczeństwo jest średnio zamożne'
        if wealth_level > 1.5 and wealth_level <= 2:
            return f'Poziom zamożności wynosi {wealth_level}. Społeczeństwo jest zamożne'
        if wealth_level > 2:
            return f'Poziom zamożności wynosi {wealth_level}. Społeczeństwo jest bardzo zamożne'

class Couple(Household):

    def __init__(self, country, city_name, cost_of_living=0,
                 cost_of_rent=0, total_cost=0, minimum_salary=0, average_salary=0, family_type='', r=1.9):
        super().__init__(country, city_name, cost_of_living, cost_of_rent, total_cost,
                         minimum_salary, average_salary, family_type, r)

    def minimum_salary_counter(self):
        self.family_type = input('Podaj rodzaj gospodarstwa domowego singiel/para/2+1/2+2: ')
        if self.family_type == 'singiel':
            self.r = 1
        if self.family_type == 'para':
            self.r = 1.9
        if self.family_type == '2+1':
            self.r = 2.7
        if self.family_type == '2+2':
            self.r = 3.5
        self.minimum_salary = (self.total_cost * 1.35) * self.r
        return f'Minimalne wynagrodzenie to: {self.minimum_salary}'

    def wealth_level_counter(self, wealth_level=0):
        if not self.family_type == 'singiel':
            multiplier = 2
        self.average_salary = float(input('Wprowadź średnie wynagrodzenie w Twoim mieście: '))
        wealth_level = round(((self.average_salary * multiplier) / self.minimum_salary), 1)
        if wealth_level <= 1:
            return f'Poziom zamożności wynosi {wealth_level}. Społeczeństwo jest mało zamożne'
        if wealth_level > 1 and wealth_level <= 1.5:
            return f'Poziom zamożności wynosi {wealth_level}. Społeczeństwo jest średnio zamożne'
        if wealth_level > 1.5 and wealth_level <= 2:
            return f'Poziom zamożności wynosi {wealth_level}. Społeczeństwo jest zamożne'
        if wealth_level > 2:
            return f'Poziom zamożności wynosi {wealth_level}. Społeczeństwo jest bardzo zamożne'

class Family2plus1(Household):

    def __init__(self, country, city_name, cost_of_living=0,
                 cost_of_rent=0, total_cost=0, minimum_salary=0, average_salary=0, family_type='', r=2.7):
        super().__init__(country, city_name, cost_of_living, cost_of_rent, total_cost,
                         minimum_salary, average_salary, family_type, r)

    def minimum_salary_counter(self):
        self.family_type = input('Podaj rodzaj gospodarstwa domowego singiel/para/2+1/2+2: ')
        if self.family_type == 'singiel':
            self.r = 1
        if self.family_type == 'para':
            self.r = 1.9
        if self.family_type == '2+1':
            self.r = 2.7
        if self.family_type == '2+2':
            self.r = 3.5
        self.minimum_salary = (self.total_cost * 1.35) * self.r
        return f'Minimalne wynagrodzenie to: {self.minimum_salary}'

    def wealth_level_counter(self, wealth_level=0):
        if not self.family_type == 'singiel':
            multiplier = 2
        self.average_salary = float(input('Wprowadź średnie wynagrodzenie w Twoim mieście: '))
        wealth_level = round(((self.average_salary * multiplier) / self.minimum_salary), 1)
        if wealth_level <= 1:
            return f'Poziom zamożności wynosi {wealth_level}. Społeczeństwo jest mało zamożne'
        if wealth_level > 1 and wealth_level <= 1.5:
            return f'Poziom zamożności wynosi {wealth_level}. Społeczeństwo jest średnio zamożne'
        if wealth_level > 1.5 and wealth_level <= 2:
            return f'Poziom zamożności wynosi {wealth_level}. Społeczeństwo jest zamożne'
        if wealth_level > 2:
            return f'Poziom zamożności wynosi {wealth_level}. Społeczeństwo jest bardzo zamożne'

class Family2plus2(Household):

    def __init__(self, country, city_name, cost_of_living=0,
                 cost_of_rent=0, total_cost=0, minimum_salary=0, average_salary=0, family_name=''):
        super().__init__(country, city_name, cost_of_living, cost_of_rent, total_cost,
                         minimum_salary, average_salary, family_name)

    def minimum_salary_counter(self):
        self.family_type = input('Podaj rodzaj gospodarstwa domowego singiel/para/2+1/2+2: ')
        if self.family_type == 'singiel':
            self.r = 1
        if self.family_type == 'para':
            self.r = 1.9
        if self.family_type == '2+1':
            self.r = 2.7
        if self.family_type == '2+2':
            self.r = 3.5
        self.minimum_salary = (self.total_cost * 1.35) * self.r
        return f'Minimalne wynagrodzenie to: {self.minimum_salary}'

    def wealth_level_counter(self, wealth_level=0):
        if not self.family_type == 'singiel':
            multiplier = 2
        self.average_salary = float(input('Wprowadź średnie wynagrodzenie w Twoim mieście: '))
        wealth_level = round(((self.average_salary * multiplier) / self.minimum_salary), 1)
        if wealth_level <= 1:
            return f'Poziom zamożności wynosi {wealth_level}. Społeczeństwo jest mało zamożne'
        if wealth_level > 1 and wealth_level <= 1.5:
            return f'Poziom zamożności wynosi {wealth_level}. Społeczeństwo jest średnio zamożne'
        if wealth_level > 1.5 and wealth_level <= 2:
            return f'Poziom zamożności wynosi {wealth_level}. Społeczeństwo jest zamożne'
        if wealth_level > 2:
            return f'Poziom zamożności wynosi {wealth_level}. Społeczeństwo jest bardzo zamożne'
