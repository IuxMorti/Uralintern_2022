import random
import string

def generate_password():
    """Созадет случайный пароль размерами от 8 до 12 символов из букв латиницы верхнего и нижнего регистра и цифр"""
    chars = string.ascii_uppercase + string.ascii_lowercase + string.digits
    size = random.randint(8, 12)
    return ''.join(random.choice(chars) for x in range(size))
