from training_data import *

# Тест на добавление тренировки
def test_add_workout():
    log = []
    result = add_workout(log, "бег", 30)
    assert result == [("бег", 30)]

# Тест на корректность подсчета общего времени
def test_total_minutes():
    log = [("бег", 30), ("отжимания", 40)]
    result = total_minutes(log)
    assert result == 70

# Проверка, работает ли множество
def test_add_kind():
    kinds_set = set()
    add_kind(kinds_set, "бег")
    add_kind(kinds_set, "бег")
    assert kinds_set == {"бег"}

# Проверка функции тренировок дольше 30 минут
def test_long_workouts():
    kinds = {
        "бег": 30,
        "отжимания": 40,
        "приседания": 20
    }
    result = long_workouts(kinds)
    assert result == ["отжимания"]


