# utils/console_output.py
from tabulate import tabulate


def print_table(data: list, headers: list):
    """
    Выводит таблицу в консоль с помощью tabulate.
    """
    # Добавляем индексы (нумерация строк)
    table_with_index = [[i + 1, row[0], row[1]] for i, row in enumerate(data)]
    print(
        tabulate(
            table_with_index, headers=[""] + headers, tablefmt="grid", floatfmt=".1f"
        )
    )
