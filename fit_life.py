# Проект FitLife - MVP версия 1.0


# 1. Функция для возраста
def get_age():
    """Получает возраст пользователя."""
    while True:
        age = int(input("Сколько тебе лет? "))

        if age > 0:
            return age
        else:
            print("Возраст должен быть больше нуля. Попробуйте снова.")


# Делала функцию для возраста с ИИ для понимания


# 2. Функция для веса
def get_weight():
    """Получает вес пользователя."""
    while True:
        weight = float(input("Сколько ты весишь (кг)? "))

        if weight > 0:
            return weight
        else:
            print("Вес должен быть больше нуля. Попробуйте снова.")


# 3. Функция для роста
def get_height():
    """Получает рост пользователя."""
    while True:
        height = float(input("Какой у тебя рост (м)? "))

        if height > 0:
            return height
        else:
            print("Рост должен быть больше нуля. Попробуйте снова.")


# 4. Функция для расчёта ИМТ
def calculate_bmi(weight, height):
    """Рассчитывает индекс массы тела."""
    bmi = weight / (height ** 2)
    return round(bmi, 1)


# 5. Функция для определения категории ИМТ
def get_bmi_category(bmi):
    """Определяет категорию ИМТ."""
    if bmi < 18.5:
        return "Ниже нормы"
    elif bmi < 25:
        return "Нормальный показатель"
    elif bmi < 30:
        return "Выше нормы"
    else:
        return "Высокий показатель"


# 6. Знакомство
print("Привет! Я твой персональный фитнес-трекер.")
user_name = input("Как тебя зовут? ")
# Использовала функцию input для получения имени


# 7. Сбор данных
user_age = get_age()
user_weight = get_weight()
user_height = get_height()


# 8. Логика расчётов
bmi = calculate_bmi(user_weight, user_height)
bmi_category = get_bmi_category(bmi)
water_liters = user_weight * 30 / 1000


# 9. Вывод результата
print(f"\nПривет, {user_name}!")
# Используем f-строку, чтобы вставлять внутрь переменные
print(f"Отчёт для пользователя: {user_name} ({user_age} г.)")
print(f"Твой ИМТ: {bmi}")
print(f"Оценка ИМТ: {bmi_category}.")
print(f"Твоя рекомендуемая норма воды: {water_liters} л. в день.")

print("\nРасчёт окончен. Будьте здоровы!")  # \n для переноса строки
