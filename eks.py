def get_days_in_month(month_name):
    months = {
        "January": 31, "February": 28, "March": 31, "April": 30,
        "May": 31, "June": 30, "July": 31, "August": 31,
        "September": 30, "October": 31, "November": 30, "December": 31
    }
    try:
        return months[month_name.capitalize()]
    except KeyError:
        raise ValueError("Invalid month name. Please provide a valid month name.")


if __name__ == "__main__":
    try:
        month = input("Enter the name of the month: ")
        days = get_days_in_month(month)
        print(f"The month of {month.capitalize()} has {days} days.")
    except ValueError as e:
        print(e)
