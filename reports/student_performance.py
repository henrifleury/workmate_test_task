# reports/student_performance.py
from typing import List, Dict, Any, Tuple
from collections import defaultdict


class StudentPerformanceReport:
    """
    Отчет: средняя оценка студента по всем предметам.
    Студенты сортируются по средней оценке (по убыванию).
    """

    headers = ["student_name", "grade"]

    def generate(self, data: List[Dict[str, Any]]) -> List[Tuple[str, float]]:
        """
        Генерирует отчет: [(имя студента, средняя оценка), ...]
        """
        grades = defaultdict(list)

        for record in data:
            student = record["student_name"]
            grade = record["grade"]
            grades[student].append(grade)

        # Считаем среднее и сортируем по убыванию
        result = [
            (student, round(sum(grade_list) / len(grade_list), 1))
            for student, grade_list in grades.items()
        ]

        result.sort(key=lambda x: x[1], reverse=True)
        return result
