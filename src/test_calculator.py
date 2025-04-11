import pytest
from calculator import City, Household


def test_cost_counter():
    city = City()
    city.cost_of_living = 1500
    city.cost_of_rent = 2000
    assert city.cost_counter() == 3500

def test_minimum_salary_counter():
    city = City()
    city.total_cost = 1000
    assert city.minimum_salary_counter() == 1350

def test_wealth_level_counter():
    household = Household()
    household.average_salary = 7500
    household.minimum_salary = 5000
    assert household.wealth_level_counter() == 1.5

# CZY TESTOWAĆ TE METODY, ALE DZIEDZICZONE W KLASACH SINGLE, COUPLE, ETC.?