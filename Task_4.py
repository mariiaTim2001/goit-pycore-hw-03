from datetime import datetime, timedelta

def get_next_workday(date: datetime.date) -> datetime.date:
    if date.weekday() == 5:
        return date + timedelta(days=2)
    elif date.weekday() == 6:
        return date + timedelta(days=1)
    return date

def get_upcoming_birthdays(users: list) -> list:
    current_date = datetime.today().date()
    upcoming_birthdays = []
    final_date = current_date + timedelta(days=7)

    for user in users:
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        current_year_birthday = birthday.replace(year=current_date.year)

        if current_year_birthday < current_date:
            current_year_birthday = current_year_birthday.replace(year=current_date.year + 1)

        if current_date <= current_year_birthday <= final_date:
            congratulation_date = get_next_workday(current_year_birthday)
            upcoming_birthdays.append({
                "name": user["name"],
                "congratulation_date": congratulation_date.strftime("%Y.%m.%d")
            })
    return upcoming_birthdays

# Test cases

# users = [
#     {"name": "John Doe", "birthday": "2025.06.15"},
#     {"name": "Jane Smith", "birthday": "2025.06.27"}
# ]

# upcoming_birthdays = get_upcoming_birthdays(users)
# print("Список привітань на цьому тижні:", upcoming_birthdays)
