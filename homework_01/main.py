"""
Домашнее задание №1
Функции и структуры данных
"""
from typing import List


def power_numbers(*numbers: int) -> list:
    """
    функция, которая принимает N целых чисел,
    и возвращает список квадратов этих чисел
    >>> power_numbers(1, 2, 5, 7)
    <<< [1, 4, 25, 49]
    """
    numbers_list: list[int] = []
    for number in numbers:
        number **= 2
        numbers_list.append(number)
    return numbers_list


# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"


def filter_numbers(numbers_list: list[int], odd_or_even_or_ptime: str) -> list:
    """
    функция, которая на вход принимает список из целых чисел,
    и возвращает только чётные/нечётные/простые числа
    (выбор производится передачей дополнительного аргумента)

    >>> filter_numbers([1, 2, 3], ODD)
    <<< [1, 3]
    >>> filter_numbers([2, 3, 4, 5], EVEN)
    <<< [2, 4]
    """
    def is_prime(a: int) -> bool:
        # делитель
        d = 2
        while d * d <= a and a % d != 0:
            d += 2
        return d * d > number
    numbers_list_for_return: list[int] = []
    if odd_or_even_or_ptime == PRIME:
        for number in numbers_list:
            if is_prime(number):
                numbers_list_for_return.append(number)
    if odd_or_even_or_ptime == ODD:
        for number in numbers_list:
            if number % 2 != 0:
                numbers_list_for_return.append(number)
    if odd_or_even_or_ptime == EVEN:
        for number in numbers_list:
            if number % 2 == 0:
                numbers_list_for_return.append(number)
    return numbers_list_for_return
