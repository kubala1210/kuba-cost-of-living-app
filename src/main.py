# from models import CityData
# from src.households import Single, Family2Plus2
# import pytest
from calculator import UserInterface
from households import (Single, Couple, Family2plus1, Family2plus2)


def main():
    single_01 = Single()
    # couple_01 = Couple()
    # family_01 = Family2plus1()
    family_02 = Family2plus2()
    history = UserInterface()
    single_01.main_calc()
    # couple_01.main_calc()
    # family_01.main_calc()
    family_02.main_calc()
    print(history.get_history())
    return False


if __name__ == "__main__":
    while True:
        try:
            main()
        except Exception as error:
            print('Błąd:', error)
            while True:
                continue_decision = (
                    input('Czy chcesz kontynuować? TAK/NIE: ')).upper()
                if continue_decision == 'TAK':
                    break
                elif continue_decision == 'NIE':
                    print('Program zakończony')
                    exit()
                else:
                    print('Wybierz tak lub nie. Inne wartości nie są przyjmowane')
                    continue
