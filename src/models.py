from pydantic import BaseModel
from typing import Dict


class CityData(BaseModel):
    name: str
    average_salary: float
    costs: Dict[str, float]
