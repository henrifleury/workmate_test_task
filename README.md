```markdown
# 📊 Student Performance Reports Generator
тестовое задание workmate:
https://docs.google.com/document/d/1Wq7ALJDhin2uY5ldh4srWQFsfJxWUZK_SK4INIwUWug/edit?tab=t.0#heading=h.or54d8e34zbk

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

## 🔧 Добавление новых отчетов

1. Создать класс отчета в `reports/`
2. Зарегистрировать в `reports/__init__.py`
