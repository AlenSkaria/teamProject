import re
from datetime import datetime

class ValidationError(Exception):
    pass


def validate_name(name):
    if not re.match(r"^[A-Za-z\s]+$", name):
        raise ValidationError(f"Invalid name: {name}. Only alphabets and spaces are allowed.")
    return True

def validate_age(age):
    if not isinstance(age, int) or age <= 0 or age > 120:
        raise ValidationError(f"Invalid age: {age}")
    return True

def validate_date(date_str, field_name):
    try:
        datetime.strptime(date_str, "%Y-%m-%d")
    except ValueError:
        raise ValidationError(f"Invalid date format for {field_name}. Use YYYY-MM-DD.")
    return True


def validate_created_on(created_on):
    validate_date(created_on, "Created On")
    if datetime.strptime(created_on, "%Y-%m-%d") > datetime.now():
        raise ValidationError(f"'createdOn' date cannot be in the future: {created_on}")
    return True


def validate_is_active(is_active):
    if not isinstance(is_active, bool):
        raise ValidationError(f"'isActive' must be a boolean value. Got: {is_active}")
    return True
    