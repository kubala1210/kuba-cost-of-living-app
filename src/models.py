import pydantic
from pydantic import BaseModel
from typing import Dict
from households import City


class CityData(BaseModel):
    country: str
    city_name: str
    minimum_salary: float
    average_salary: float
    cost_of_living: float
    cost_of_rent: float

verify_data = CityData(country='Poland', city_name='Wroclaw',
                       minimum_salary=5500, average_salary=7500, cost_of_living=2500, cost_of_rent=3000)

print(verify_data)
print(f"Total cost of living: {verify_data.cost_of_living + verify_data.cost_of_rent}")