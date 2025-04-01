# Aplikacja: Analiza kosztów życia w miastach

## Cel projektu

Aplikacja analizuje koszty życia w wybranych miastach i oblicza minimalne wynagrodzenie potrzebne do życia w zależności od typu gospodarstwa domowego. 
Na tej podstawie obliczany jest również wskaźnik zamożności społeczeństwa.

Projekt uczy:
- Pracy z danymi wejściowymi
- Programowania obiektowego (klasy, dziedziczenie, polimorfizm)
- Struktury aplikacji i dzielenia kodu na moduły
- Obsługi błędów i walidacji danych

---

## Zasada działania

Program:
1. Pobiera dane o kosztach życia i średnich zarobkach (z pliku lub API)
2. Oblicza koszt życia w mieście
3. Oblicza minimalne potrzebne wynagrodzenie
4. Porównuje z wynagrodzeniem średnim i oblicza wskaźnik zamożności
5. Wyświetla wynik użytkownikowi

---

## Struktura programu

Program oparty jest o klasy i dziedziczenie:

### Klasa bazowa `Household`
Reprezentuje gospodarstwo domowe. Zawiera metody wspólne dla wszystkich grup (np. formatowanie wyniku).

### Klasy dziedziczące `Single`, `Couple`, `Family2Plus1`, `Family2Plus2`
Każda klasa definiuje swoją wartość do obliczenia kosztu minimalnego wynagrodzenia.

## Zewnętrzne biblioteki

W tym projekcie użyjemy zewnętrznych bibliotek Pythona:

### `requests`
Służy do pobierania danych z API. Kursant nauczy się:
- Jak wysłać zapytanie HTTP GET
- Jak sparsować odpowiedź JSON
- Jak obsłużyć błędy połączenia

Dokumentacja: https://docs.python-requests.org/

### `pydantic` (opcjonalnie)
Służy do walidacji danych i pracy z modelami (klasy danych).
To nowa dla Ciebie biblioteka i trzeba nauczyć się jej działania z dokumentacji.

Dokumentacja: https://docs.pydantic.dev/

---

## Model danych

Wprowadź model danych reprezentujący dane o mieście. Użyj `pydantic.BaseModel`:

```python
from pydantic import BaseModel, Field
from typing import Dict

class CityData(BaseModel):
    name: str
    average_salary: float
    costs: Dict[str, float]
```

## TODO (zadania)

### Etap 1 – Podstawowa aplikacja
- [ ] Stwórz klasy `City`, `Household`, `Single`, `Couple`, `Family2Plus1`, `Family2Plus2`
- [ ] Stwórz klasę `CostCalculator`, która przyjmuje `City` i `Household`
- [ ] Oblicz koszt życia na podstawie danych
- [ ] Oblicz minimalne wynagrodzenie
- [ ] Oblicz i opisz wskaźnik zamożności

---

### Etap 2 – Nauka dziedziczenia i polimorfizmu
- [ ] Zaimplementuj wspólne metody w klasie `Household`
- [ ] W klasach potomnych (`Single`, `Couple`, itd.) tylko różnicuj wartość `R`
- [ ] Używaj klasy `Household` polimorficznie w `CostCalculator` (bez sprawdzania typu)

---

### Etap 3 – Obsługa błędów (różne wyjątki)
- [ ] Obsłuż wyjątki: `KeyError`, `TypeError`, `ValueError`, `ZeroDivisionError`
- [ ] Wyjaśnij w komentarzu, że wszystkie dziedziczą po `Exception`
- [ ] Użyj `try/except` w kilku miejscach, żeby zabezpieczyć aplikację

---

### Etap 4 – Walidacja danych z modelu
- [ ] Użyj `pydantic.BaseModel` do reprezentacji danych o mieście
- [ ] Sprawdź, czy dane są poprawne (np. czy wszystkie koszty to liczby dodatnie)
- [ ] Obsłuż wyjątki walidacyjne (`ValidationError` w przypadku `pydantic`)

---

### Etap 5 – Pobieranie danych z API
- [ ] Skorzystaj z `requests`, by pobrać dane z wybranego API
- [ ] Parsuj odpowiedź JSON i przekształć ją do modelu `City`
- [ ] Obsłuż błędy sieciowe i HTTP (`requests.exceptions.RequestException`)

---

### Etap 6 – Zapis i odczyt danych z pliku
- [ ] Zapisz dane miasta do pliku `.json` (`save_city_data`)
- [ ] Obsłuż wyjątki: `FileNotFoundError`, `IOError`, `JSONDecodeError`

---

### Etap 7 – Logowanie i wynik działania
- [ ] Zapisz wynik obliczeń oraz to co zwraca api do pliku (np. `output.json` lub `.txt`)
- [ ] Loguj błędy do osobnego pliku (np. `errors.log`)

---
