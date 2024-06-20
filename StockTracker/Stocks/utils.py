# utils.py

import random
import string

def generate_otp():
    # Generate a random OTP (6-digit)
    return ''.join(random.choices(string.digits, k=6))
