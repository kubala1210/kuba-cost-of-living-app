from pydantic import BaseModel, ValidationError
from calculator import UserInterface, City, Household


class CityData(BaseModel):
    family_type: str
    country: str
    city_name: str
    cost_of_living: float
    cost_of_rent: float
    average_salary: float
    multiplier: float

    def validate_data(self, family_type, country, city_name, cost_of_living, cost_of_rent, average_salary, multiplier):
        if (any(char.isdigit() for char in city_name)
                or any(char.isdigit() for char in country)):
            raise TypeError('Nazwa państwa i miasta nie moze zawierać cyfr')
        if cost_of_living <= 0:
            raise ValueError('Koszt życia nie może być mniejszy lub równe 0')
        if cost_of_rent <= 0:
            raise ValueError(
                'Koszt wynajmu lub kredytu nie może być mniejszy lub równe 0')
        if average_salary <= 0:
            raise ValueError(
                'Średnie wynagrodzenie nie moze być mniejsze lub równe 0')
