# from models import CityData
# from src.households import Single, Family2Plus2
from calculator import (Single, Couple, Family2plus1, Family2plus2)


def main():
    single_01 = Single()
    couple_01 = Couple()
    family_01 = Family2plus1()
    family_02 = Family2plus2()

    single_01.main_calc()
    couple_01.main_calc()
    family_01.main_calc()
    family_02.main_calc()
    pass


if __name__ == "__main__":
    main()
