# main.py
import argparse
import sys
from core.data_loader import load_data
from reports import get_report
from utils.console_output import print_table


def main():
    parser = argparse.ArgumentParser(
        description="Скрипт для формирования отчетов по успеваемости студентов."
    )
    parser.add_argument(
        "--files", nargs="+", required=True, help="Пути к CSV-файлам с данными"
    )
    parser.add_argument(
        "--report", required=True, help="Тип отчета (например, student_perf)"
    )

    args = parser.parse_args()

    # Загрузка данных из всех файлов
    data = load_data(args.files)

    # Получение нужного отчета
    report_class = get_report(args.report)
    if report_class is None:
        print(f"Ошибка: отчет '{args.report}' не найден.", file=sys.stderr)
        sys.exit(1)

    report = report_class()
    result = report.generate(data)

    # Вывод в консоль
    print_table(result, headers=report.headers)


if __name__ == "__main__":
    main()
