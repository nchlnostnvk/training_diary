import training_data as td

# Переменные для хранения тренировок и времени
log = ""
total_min = 0

# Основной цикл программы
while True:
    command = input("> ").strip()

    if command == "exit":
        print("Программа завершена.")
        break

    elif command == "motivate":
        print(td.random_motivation())

    elif command == "help":
        td.show_help()

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

        # Добавляем тренировку и обновляем время
        log = td.add_workout(log, exercise, minutes)
        total_min = td.total_minutes(total_min, minutes)

        print(f"Тренировка {exercise} добавлена.")

    elif command == "list":
        print(log if log else "Дневник пуст.")

    elif command == "total":
        print(f"Общее время: {total_min} минут")

    else:
        print("Неизвестная команда.")




