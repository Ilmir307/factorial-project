"""Числа Фибоначчи (новая функциональность ветки feature/fibonacci)."""


def fibonacci(n):
    """Возвращает список первых n чисел Фибоначчи."""
    numbers = []
    a, b = 0, 1
    for _ in range(n):
        numbers.append(a)
        a, b = b, a + b
    return numbers
