from calculator import UserInterface, City, Household, History
from models import CityData
from pydantic import ValidationError
import json


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
                                     cost_of_living, cost_of_rent, average_salary, multiplier)

        calc_cost = City(validated_data)
        total_cost = calc_cost.cost_counter()
        minimum_salary = calc_cost.minimum_salary_counter(total_cost)

        calc_wealth_level = Household(validated_data)
        wealth_level = calc_wealth_level.wealth_level_counter(minimum_salary)
        calc_wealth_level.display_wealth_level(wealth_level)

        return (family_type, country, city_name, cost_of_living,
                cost_of_rent, average_salary, minimum_salary, total_cost, wealth_level)

    except TypeError as e:
        print('Błąd typu danych', e)
    except ValidationError as e:
        print('Błąd walidacji danych', e)
    except Exception as e:
        print('Nieoczkiwany błąd', e)


if __name__ == "__main__":
    calc_history = History()

    while True:
        try:
            (family_type, country, city_name, cost_of_living, cost_of_rent,
             average_salary, minimum_salary, total_cost, wealth_level) = main()
            calc_history.save_calc_data(family_type, country, city_name, cost_of_living, cost_of_rent,
             average_salary, minimum_salary, total_cost, wealth_level)
        except Exception as error:
            calc_history.save_error_history(error)
            print('Błąd:', error)
        continuation = (input('Czy chcesz kontynuować? TAK/NIE ')).upper()
        if continuation == 'NIE':
            json_history = json.dumps(calc_history.calc_history, indent=4)
            error_history = json.dumps(calc_history.error_history, indent=4)
            print(json_history, error_history)
            exit()
        else:
            continue
