import re
from datetime import datetime

def get_days_from_today(date: str = None) -> str:
    if date is None:
        return "Error! Date cannot be None."
    if not isinstance(date, str):
        return "Error! Date must be a string in format YYYY-MM-DD."
    if not re.match(r'^\d{4}-\d{2}-\d{2}$', date):
        return "Date must be in the format YYYY-MM-DD."
   
    try:
        user_date = datetime.strptime(date, '%Y-%m-%d').date()
    except ValueError:
        return "Error! This date does not exist."
    
    current_date = datetime.today().date()
    delta_days = current_date - user_date
    return delta_days.days

# Test cases
# print(get_days_from_today("0000-00-00")) 
# print(get_days_from_today()) 
# print(get_days_from_today("2023-10-01"))
# print(get_days_from_today(1))
# print(get_days_from_today(True))
# print(get_days_from_today("2023-00-01"))
# print(get_days_from_today("2023-02-30"))
# print(get_days_from_today("2023-10-01"))
# print(get_days_from_today("0000-00-00"))
# print(get_days_from_today("2023/10/01"))
# print(get_days_from_today(""))
# print(get_days_from_today("2020-01-01"))
# print(get_days_from_today("2050-01-01"))
