import random

MOTIVATION = [
"Каждая тренировка приближает тебя к цели!",
"Дисциплина важнее мотивации!",
"Сегодня ты сильнее, чем вчера!",
"Не останавливайся на достигнутом!"
]

# Возвращает случайную мотивационную фразу
def random_motivation():
    return random.choice(MOTIVATION)

# Показывает список доступных команд
def show_help():
    print("""
Доступные команды:
add <вид> <минуты> — добавить тренировку
list — показать тренировки
total — общее время тренировок
motivate — мотивационная фраза
help — показать справку
exit — выход
    """)

# Добавляет тренировку в строку дневника в виде кортежа
def add_workout(log, kind, minutes):
    log.append((kind, minutes))
    return log

# Возвращает обновлённое общее время
def total_minutes(log):
    total = 0
    for kind, minutes in log:
        total += minutes
    return total

# Добавляет тренировку в множество
def add_kind(kinds_set, k):
    kinds_set.add(k)
    return kinds_set

# Создает список из тренировок, продолжительность которых > 30 минут
def long_workouts(kinds):
    return [k for k, m in kinds.items() if m > 30]

# Выводит названия тренировок заглавными буквами
def upper_kinds(kinds):
    return [k.upper() for k in kinds]
