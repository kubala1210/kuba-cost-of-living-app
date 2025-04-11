from calculator import UserInterface, City, Household
from models import CityData
from pydantic import ValidationError

def main():
    data_01 = UserInterface()
    (family_type, country, city_name, cost_of_living,
     cost_of_rent, average_salary, multiplier) = data_01.collect_data()

    try:
        validated_data = CityData(family_type=family_type, country=country,
                                  city_name=city_name, cost_of_living=cost_of_living,
                                  cost_of_rent=cost_of_rent, average_salary=average_salary,
                                  multiplier=multiplier)
        validated_data.validate_data(family_type, country, city_name,
                                     cost_of_living,cost_of_rent, average_salary, multiplier)

        calc_cost = City(validated_data)
        total_cost = calc_cost.cost_counter()
        minimum_salary = calc_cost.minimum_salary_counter(total_cost)

        calc_wealth_level = Household(validated_data)
        wealth_level = calc_wealth_level.wealth_level_counter(minimum_salary)
        calc_wealth_level.display_wealth_level(wealth_level)

    except TypeError as e:
        print('Błąd typu danych', e)
    except ValidationError as e:
        print('Błąd walidacji danych', e)
    except Exception as e:
        print('Nieoczkiwany błąd', e)


if __name__ == "__main__":
        try:
            main()
        except Exception as error:
            print('Błąd:', error)