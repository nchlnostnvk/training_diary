from training_data import WORKOUT_TYPES
import random

# Переменные для хранения тренировок и времени
log = ""
total_min = 0

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

# Основной цикл программы
while True:
    command = input("> ").strip()

    if command == "exit":
        print("Программа завершена.")
        break

    elif command == "motivate":
        print(random_motivation())

    elif command == "help":
        show_help()

    elif command.startswith("add "):
        # Отделяем название тренировки от минут
        parts = command[4:].rsplit(" ", 1)

        if len(parts) < 2:
            print("Укажите название тренировки и количество минут.")
            continue

        exercise = parts[0].strip()
        minutes_str = parts[1].strip()

        # Проверяем название тренировки
        if exercise == "":
            print("Укажите название тренировки.")
            continue

        # Преобразуем минуты в число
        try:
            minutes = int(minutes_str)
        except ValueError:
            print("Количество минут должно быть числом.")
            continue

        # Проверяем положительность времени
        if minutes <= 0:
            print("Количество минут должно быть больше нуля.")
            continue

        # Проверяем допустимый вид тренировки
        if exercise.lower() not in WORKOUT_TYPES.lower():
            print("Неизвестный вид тренировки.")
            print("Доступные виды:", WORKOUT_TYPES)
            continue

        # Добавляем тренировку и обновляем время
        log = add_workout(log, exercise, minutes)
        total_min = total_minutes(total_min, minutes)

        print(f"Тренировка {exercise} добавлена.")

    elif command == "list":
        print(log if log else "Дневник пуст.")

    elif command == "total":
        print(f"Общее время: {total_min} минут")

    else:
        print("Неизвестная команда.")




