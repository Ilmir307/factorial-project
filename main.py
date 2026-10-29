"""Точка входа демо-проекта factorial-project (задание 1839)."""

from factorial import factorial


def main():
    """Считает и печатает факториалы нескольких чисел."""
    for number in (0, 5, 10):
        print(str(number) + "! =", factorial(number))


if __name__ == "__main__":
    main()
