import random

# Возвращает случайную мотивационную фразу
def random_motivation():
    random_number = random.randint(1, 4)

    if random_number == 1:
        return "Каждая тренировка приближает тебя к цели!"
    elif random_number == 2:
        return "Дисциплина важнее мотивации!"
    elif random_number == 3:
        return "Сегодня ты сильнее, чем вчера!"
    else:
        return "Не останавливайся на достигнутом!"


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


# Добавляет тренировку в строку дневника
def add_workout(log, kind, minutes):
    if log:
        log += ", "

    log += kind + " — " + str(minutes) + " мин"
    return log


# Возвращает обновлённое общее время
def total_minutes(current, minutes):
    return current + minutes
