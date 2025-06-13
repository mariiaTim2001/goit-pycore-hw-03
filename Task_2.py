import random

def get_numbers_ticket(min: int, max: int, quantity: int) -> list:
    if not isinstance(min, int) or not isinstance(max, int) or not isinstance(quantity, int):
        return [], "Error! All parameters must be integers."
    if min < 1 or min >= max:
        return [], "Error! Minimum must be less than maximum and must be greater than 0."
    if max > 1000:
        return [], "Error! Maximum must be less than or equal to 1000."
    if quantity <= 0:
        return [], "Error! Quantity must be a positive integer."
    if quantity > (max - min + 1):
        return [], "Error! Cannot generate {} unique numbers in range [{}, {}].".format(quantity, min, max)
    
    numbers = set()
    while len(numbers) < quantity:
        numbers.add(random.randint(min, max))
    
    return sorted(numbers)
# Test cases
# print(get_numbers_ticket(1, 10, 5))
# print(get_numbers_ticket(1, 10, 0))
# print(get_numbers_ticket(10, 1, 5))
# print(get_numbers_ticket(1, 10, -5))
# print(get_numbers_ticket(1, 6, 10))
# print(get_numbers_ticket("111", "10", "5"))
# print(get_numbers_ticket(1, True, None))