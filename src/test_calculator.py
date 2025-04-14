import pytest
from calculator import City, Household
from models import CityData

@pytest.fixture
def sample_validated_data():

    validated_data = CityData(family_type='COUPLE', country='Poland',
                              city_name='Wroclaw', cost_of_living=2500,
                              cost_of_rent=3000, average_salary=7500,
                              multiplier=1.9)
    return validated_data

@pytest.fixture
def sample_wrong_data():
    wrong_data = CityData(family_type='COUPLE', country='Poland',
                              city_name='Wroclaw', cost_of_living=-2500,
                              cost_of_rent=3000, average_salary=7500,
                              multiplier=1.9)
    return wrong_data

def test_cost_counter(sample_validated_data):
    city = City(sample_validated_data)
    city.cost_of_living = 1500
    city.cost_of_rent = 2000
    assert city.cost_counter() == 3500

def test_validation(sample_wrong_data):
    with pytest.raises(ValueError):
        sample_wrong_data.validate_data(sample_wrong_data.family_type, sample_wrong_data.country,
                                        sample_wrong_data.city_name, sample_wrong_data.cost_of_living,
                                        sample_wrong_data.cost_of_rent, sample_wrong_data.average_salary,
                                        sample_wrong_data.multiplier)


def test_minimum_salary_counter(sample_validated_data):
    city = City(sample_validated_data)
    assert city.minimum_salary_counter(1000) == 2565


def test_wealth_level_counter(sample_validated_data):
    household = Household(sample_validated_data)
    assert household.wealth_level_counter(5000) == 2.9
