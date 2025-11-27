# Zack Oakley
# 11/27/2025
# File exists to expose .env variables to other functions

import os
from dotenv import load_dotenv

# Load variables from .env into environment
load_dotenv()

# Reads and returns the EQ_MAGNITUDE_THRESHOLD env var, defaults to 5 if undefined
def get_magnitude_threshold():
    value = os.getenv("EQ_MAGNITUDE_THRESHOLD", "5.0")
    return float(value)

# Reads and returns EMAIL_USER env var
def get_email_user():
    return os.getenv("EMAIL_USER")

# Reads and returns EMAIL_PASS env var
def get_email_password():
    return os.getenv("EMAIL_PASS")

# Reads and returns the EMAIL_TO env var
def get_email_to():
    return os.getenv("EMAIL_TO")

# Reads and returns the SMTP_SERVER env var, defaults to smtp.gmail.com if underfined
def get_smtp_host():
    return os.getenv("SMTP_SERVER", "smtp.gmail.com")

# Reads and returns the SMTP_PORT env var, defaults to 587 if undefined
def get_smtp_port():
    return int(os.getenv("SMTP_PORT", "587"))