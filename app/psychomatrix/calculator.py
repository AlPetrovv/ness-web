from datetime import datetime

from .models import PsychomatrixBaseContent, PsychomatrixAdditionalContent


class Calculator:

    def __init__(self, date: datetime):
        self.date = date

    def __get_birth_numbers(self) -> list[int]:
        """
        :return: list; example [16, 4, 1998]
        """
        return [self.date.day, self.date.month, self.date.year]

    def __get_birth_additional_numbers(self) -> list[int]:
        """
        :return: list; example [38, 11, 36, 9]
        """
        date_to_string = "".join(str(n) for n in self.__get_birth_numbers())
        first_numbers = sum(map(int, date_to_string))

        second_numbers = (
            first_numbers if first_numbers < 13
            else sum(map(int, str(first_numbers)))
        )
        third_numbers = (
            first_numbers - (2 * int(str(self.date.day)[0]))
            if self.date.year < 2000 else first_numbers + 19
        )
        fourth_numbers = (
            third_numbers if third_numbers < 13
            else sum(map(int, str(third_numbers)))
        )

        return [first_numbers, second_numbers, third_numbers, fourth_numbers]

    def __get_all_birth_numbers(self) -> list[int]:
        """
        :return: list; example [16, 4, 1998, 38, 11, 36, 9]
        """
        return self.__get_birth_numbers() + self.__get_birth_additional_numbers()

    def get_numbers(self) -> list[str]:
        """
        :return: list; example ['1111', '-', '33', '4', '-', '66', '-', '88', '999']
        """
        numbers = str(self.__get_all_birth_numbers())

        square_numbers = [
            ''.join(
                str(num) for _ in range(0, numbers.count(str(num)))
            ) if str(num) in numbers else '-' for num in range(1, 10)
        ]

        return square_numbers

    def get_additional_numbers(self) -> list[str]:
        """
        :return: list; example ['6', '3', '5', '2', '5', '2', '7', '7']
        """
        basic_numbers = self.get_numbers()

        def calculate(index: tuple):
            num = len((basic_numbers[index[0]] +
                       basic_numbers[index[1]] +
                       basic_numbers[index[2]]
                       ).replace('-', ''))

            return str(num) if num > 0 else '-'

        return [calculate((0, 1, 2)), calculate((3, 4, 5)), calculate((6, 7, 8)),
                calculate((2, 4, 6)), calculate((0, 3, 6)),
                calculate((1, 4, 7)), calculate((2, 5, 8)), calculate((0, 4, 8))]

    def get_all_numbers(self) -> list[str]:
        """
        :return: list; example
        ['1111', '-', '33', '4', '-', '66', '-', '88', '999', '6', '3', '5', '2', '5', '2', '7', '7']
        """
        return self.get_numbers() + self.get_additional_numbers()


def get_contents(numbers: list) -> tuple[list, list]:
    basic_codes = [
        f'{enum}-нет' if num == '-' else num for enum, num in
        enumerate(numbers[:9], start=1)
    ]
    additional_codes = [
        f'{enum}-0' if num == '-' else f'{enum}-{num}'
        if enum not in [8, 3] else f'{enum}-'
        for enum, num in
        enumerate(numbers[9:], start=1)
    ]

    basic_contents = PsychomatrixBaseContent.objects.filter(
        code__in=basic_codes
    )
    additional_codes = PsychomatrixAdditionalContent.objects.filter(
        code__in=additional_codes
    )
    basic = [{'name': item.title, 'number': item.code, 'description': item.text} for item in basic_contents]
    additional = [{'name': item.title, 'number': item.code, 'description': item.text} for item in additional_codes]

    return basic, additional
