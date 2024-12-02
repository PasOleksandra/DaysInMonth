def get_days_in_month(month_name):
    # Словник з місяцями та їх кількістю днів
    months = {
        "January": 31, "February": 28, "March": 31, "April": 30,
        "May": 31, "June": 30, "July": 31, "August": 31,
        "September": 30, "October": 31, "November": 30, "December": 31
    }
    try:
        # Повертаємо кількість днів у введеному місяці
        return months[month_name.capitalize()]
    except KeyError:
        # Генеруємо виключення у разі неправильного введення
        raise ValueError("Invalid month name. Please provide a valid month name.")

# Основний блок програми
if __name__ == "__main__":
    try:
        # Введення користувачем назви місяця
        month = input("Enter the name of the month: ")
        days = get_days_in_month(month)
        print(f"The month of {month.capitalize()} has {days} days.")
    except ValueError as e:
        # Обробка виключення
        print(e)
