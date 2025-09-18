# tests/test_student_performance.py
import pytest
from reports.student_performance import StudentPerformanceReport


def test_student_performance_report():
    report = StudentPerformanceReport()
    data = [
        {"student_name": "Иванов Алексей", "subject": "Математика", "grade": 4.0},
        {"student_name": "Иванов Алексей", "subject": "Физика", "grade": 5.0},
        {"student_name": "Петров Дмитрий", "subject": "Математика", "grade": 3.0},
        {"student_name": "Петров Дмитрий", "subject": "Физика", "grade": 4.0},
    ]

    result = report.generate(data)

    assert result == [
        ("Иванов Алексей", 4.5),
        ("Петров Дмитрий", 3.5),
    ]


def test_single_student():
    report = StudentPerformanceReport()
    data = [
        {"student_name": "Соколов Павел", "subject": "Химия", "grade": 4.8},
        {"student_name": "Соколов Павел", "subject": "Биология", "grade": 4.8},
    ]
    result = report.generate(data)
    assert result == [("Соколов Павел", 4.8)]


def test_empty_data():
    report = StudentPerformanceReport()
    result = report.generate([])
    assert result == []
