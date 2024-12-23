"""
Moduł tworzy listę słowników opisujących osoby, a następnie wybiera osoby spełniające zadane kryteria.
"""

if __name__ == '__main__':

    # Dane wejściowe
    osoba1 = {
        'imie': 'Tomasz',
        'nazwisko': 'Kowalski',
        'adres': 'Poznań',
        'plec': True,
        'wiek': 22
    }
    osoba2 = {
        'imie': 'Anna',
        'nazwisko': 'Ściborek',
        'adres': 'Szczecin',
        'plec': False,
        'wiek': 18
    }
    osoba3 = {
        'imie': 'Łukasz',
        'nazwisko': 'Kowalski',
        'adres': 'Wrocław',
        'plec': True,
        'wiek': 30
    }
    osoba4 = {
        'imie': 'Alicja',
        'nazwisko': 'Tarnowska',
        'adres': 'Poznań',
        'plec': False,
        'wiek': 25
    }

    lista_osob = [osoba1, osoba2, osoba3, osoba4]

    # Przykład 1: Lista mężczyzn mieszkających w Poznaniu
    poznaniacy = [osoba for osoba in lista_osob if osoba['plec'] and osoba['adres'] == 'Poznań']
    print('1. Lista poznaniaków:', *poznaniacy, sep='\n', end='\n\n')

    # Przykład 2: Lista dwudziestolatków
    dwudziestoletni = [osoba for osoba in lista_osob if 20 <= osoba['wiek'] < 30]
    print('2. Lista dwudziestolatków i dwudziestolatek:', *dwudziestoletni, sep='\n', end='\n\n')

    # Przykład 3: Średnia wieku kobiet o imionach rozpoczynających się na 'A'
    lista_wieku_kobiet_na_A = [osoba['wiek'] for osoba in lista_osob if not osoba['plec'] and osoba['imie'].startswith('A')]
    # zamiast:
    #    osoba['imie'].startswith('A')
    # można też napisać:
    #    osoba['imie'][0] == 'A'

    # Upewniamy się, że przynajmniej jedna osoba spełnia zadane kryteria
    if lista_wieku_kobiet_na_A:
        srednia_wieku = sum(lista_wieku_kobiet_na_A) / len(lista_wieku_kobiet_na_A)
        print('3. Średnia wieku kobiet o imionach zaczynających się na \'A\':', srednia_wieku)

        # W ostatnim przykładzie do wyliczenia średniej można także użyć funkcji mean z pakietu statistics
        #
        # import statistics
        # print('Średnia wieku kobiet o imionach na A...:', statistics.mean(lista_wieku_kobiet_na_A))
