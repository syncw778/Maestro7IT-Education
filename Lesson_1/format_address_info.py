def format_address_info():
    """
    Форматирует информацию об адресе в читаемый вид.
    
    Пример вывода:
    
    country: rus
    city: moscow
    zip_code: 99608
    floor: 10
    has_intercom: True
    
    Returns:
        str: Отформатированная строка с информацией об адресе
    """
    country = "rus"
    city = "moscow"
    zip_code = "99608"
    floor = "10"
    has_intercom = True  # True or False

    return f"""
country: {country}
city: {city}
zip_code: {zip_code}
floor: {floor}
has_intercom: {has_intercom}
"""

# Пример использования
print(format_address_info().strip())  # .strip() убирает лишние переносы в начале и конце