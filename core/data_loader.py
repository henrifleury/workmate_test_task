# core/data_loader.py
import csv
from typing import List, Dict, Any


def load_data(file_paths: List[str]) -> List[Dict[str, Any]]:
    """
    Загружает данные из списка CSV-файлов.
    Возвращает список словарей (каждая строка — словарь).
    """
    data = []
    for file_path in file_paths:
        try:
            with open(file_path, mode="r", encoding="utf-8") as f:
                reader = csv.DictReader(f)
                for row in reader:
                    # Преобразуем grade в float
                    row["grade"] = float(row["grade"])
                    data.append(row)
        except FileNotFoundError:
            print(f"Ошибка: файл {file_path} не найден.", file=sys.stderr)
            sys.exit(1)
        except ValueError as e:
            print(
                f"Ошибка: некорректное значение в файле {file_path}: {e}",
                file=sys.stderr,
            )
            sys.exit(1)
    return data
