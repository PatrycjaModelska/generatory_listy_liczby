from decimal import Decimal


# ZADANIE 1. GENERATOR KODÓW POCZTOWYCH
# przyjmuje 2 stringi: "79-900" i "80-155" i zwraca listę kodów pomiędzy nimi

def generator(first_postcode, second_postcode):
    for element in range(int(first_postcode.replace("-", "")) + 1, int(second_postcode.replace("-", ""))):
        yield str(element)[0:2] + "-" + str(element)[2:]


mygen = generator("79-900", "80-155")
print(list(mygen))


# ZADANIE 2. PODANA JEST LISTA ZAWIERAJĄCA ELEMENTY O WARTOŚCIACH 1-n. NAPISZ FUNKCJĘ KTÓRA SPRAWDZI JAKICH ELEMENTÓW BRAKUJE
# 1-n = [1,2,3,4,5,...,10]
# np. n=10
# wejście: [2,3,7,4,9], 10
# wyjście: [1,5,6,8,10]

def check_missing_numbers(numbers, n):
    # I version - operate on lists only
    # missing_numbers = []
    # for element in range(1, n + 1):
    #     if element not in numbers:
    #         missing_numbers.append(element)

    # II version - sets
    missing_numbers = list(set(range(1, n + 1)) - set(numbers))

    return missing_numbers


print(check_missing_numbers([2, 3, 7, 4, 9], 10))


# ZADANIE 3. NALEŻY WYGENEROWAĆ LISTĘ LICZB OD 2 DO 5.5 ZE SKOKIEM CO 0.5, DANE WYNIKOWE MUSZĄ BYĆ TYPU DECIMAL.

def decimal_range():
    # I version
    # start = Decimal(2)
    # step = Decimal(0.5)
    # temporary_list = [start]
    # while start < Decimal(5.5):
    #     start = Decimal(start) + step
    #     temporary_list.append(start)
    # return temporary_list

    # II version - math/list comprehension
    return [Decimal(4 + x) / 2 for x in range(8)]


print(decimal_range())
