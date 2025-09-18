# 📊 Student Performance Reports Generator

```markdown
# 📊 Генератор отчетов успеваемости студентов

Python-скрипт для формирования отчетов из CSV файлов с данными об успеваемости.

## 🚀 Возможности

- Чтение нескольких CSV файлов
- Красивые таблицы в консоли
- Легкое добавление новых отчетов
- Полное покрытие тестами
- Обработка ошибок

## 📦 Установка

```bash
pip install -r requirements.txt
или
pip install -r requirements-dev.txt
```

## 💻 Использование

```bash
python main.py --files students1.csv students2.csv --report student_perf
```

### Параметры:
- `--files` - пути к CSV файлам
- `--report` - тип отчета (пока только `student_perf`)

## 🏗️ Структура проекта

```
project/
├── main.py
├── core/           # Загрузка данных
├── reports/        # Генераторы отчетов  
├── utils/          # Вспомогательные функции
└── tests/          # Тесты
```

## 🧪 Тестирование

```bash
pytest tests/ -v
pytest --cov=. --cov-report=term-missing
```

## 🔧 Добавление новых отчетов

1. Создать класс отчета в `reports/`
2. Зарегистрировать в `reports/__init__.py`
3. Добавить обработку данных в `core/data_loader.py`
4. Написать тесты

## 📄 Формат CSV

```csv
student_name,subject,teacher_name,date,grade
Иванов Иван,Математика,Петров Пётр,2023-10-10,5
```

---

⭐ Если проект полезен - поставьте звездочку!
```
