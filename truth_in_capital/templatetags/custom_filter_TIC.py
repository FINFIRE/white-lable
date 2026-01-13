from django import template

register = template.Library()

@register.filter
def get_item(dictionary, key):
    """Fetch a value from a dictionary using a dynamic key."""
    return dictionary.get(key)

@register.filter
def sum_values(values_list):
    """Sum all numeric values in a list, handling None and non-numeric values."""
    if not values_list:
        return 0
    
    total = 0
    for value in values_list:
        if value is not None:
            try:
                # Convert to float first to handle both int and float values
                numeric_value = round(float(value), 2)
                total += round(float(numeric_value), 2)
            except (ValueError, TypeError):
                # Skip non-numeric values
                continue
    
    return total

@register.filter
def multiply(value, multiplier):
    """Multiply a value by a multiplier."""
    try:
        return float(value) * float(multiplier)
    except (ValueError, TypeError):
        return 0

@register.filter
def add(value1, value2):
    """Add two values together."""
    try:
        return float(value1) + float(value2)
    except (ValueError, TypeError):
        return 0