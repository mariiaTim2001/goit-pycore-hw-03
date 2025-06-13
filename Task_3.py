import re

def normalize_phone(phone_number: str) -> str:
    if not isinstance(phone_number, str):
        return "Error! Phone number must be a string."
    
    digits = re.sub(r'[^\d+]', '', phone_number)

    if len(phone_number) < 10:
        return "Error! Phone number must be at least 10 characters long."
    
    if digits.startswith('+'):
        return digits
    else:
        if digits.startswith('380'):
            return '+' + digits
        else:
            return '+38' + digits
        
# Test cases
# raw_numbers = [
#     "    +38(050)123-32-34",
#     "     0503451234",
#     "(050)8889900",
#     "38050-111-22-22",
#     "38050 111 22 11   ",
#      "067\\t123 4567",
#     "(095) 234-5678\\n",
#     "+380 44 123 4567",
#     "380501234567",
#     "    +38(050)123-32-34",
#     "     0503451234",
#     "(050)8889900",
#     "38050-111-22-22",
#     "38050 111 22 11   ",
# ]

# sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
# print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)
