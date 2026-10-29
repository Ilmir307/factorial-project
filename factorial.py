"""Вычисление факториала числа (проект factorial-project, задание 1839)."""


def factorial(n):
    """Возвращает факториал неотрицательного целого числа n.

    Для отрицательных чисел выбрасывает ValueError.
    """
    if n < 0:
        raise ValueError("факториал определён только для n >= 0")
    result = 1
    for i in range(2, n + 1):
        result = result * i
    return result
