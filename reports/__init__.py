# reports/__init__.py
#from reports.student_performance import StudentPerformanceReport
from .student_performance import StudentPerformanceReport

REPORTS = {
    "student_perf": StudentPerformanceReport,
    # Добавьте сюда другие отчеты: "teacher_perf", "course_perf" и т.д.
}


def get_report(name: str):
    """Возвращает класс отчета по имени."""
    return REPORTS.get(name)
