log = ""
total_min = 0
while True:
    command = input("> ").strip()
    if command == "exit":
        break
    elif command.startswith("add "):
        parts = command[4:].rsplit(" ", 1)
        if len(parts) < 2:
            print("Укажите название тренировки и количество минут.")
            continue
        exercise = parts[0].strip()
        minutes_str = parts[1].strip()
        if exercise == "":
            print("Укажите название тренировки.")
            continue
        try:
            minutes = int(minutes_str)
        except ValueError:
            print("Количество минут должно быть числом.")
            continue
        if minutes <= 0:
            print("Количество минут должно быть больше нуля.")
            continue
        if exercise in log.split(", "):
            print(f"Тренировка {exercise} уже есть в списке.")
            continue
        if log:
            log += ", "
        log += exercise
        total_min += minutes
        print(f"Тренировка {exercise} добавлена.")
    elif command == "list":
        print(log if log else "Дневник пуст.")
    elif command == "total":
        print(f"Общее время: {total_min} минут")
    else:
        print("Неизвестная команда.")



