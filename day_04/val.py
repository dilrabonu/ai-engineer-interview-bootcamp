class ValidationError(Exception):
    """ Custome error for validation failures"""
    pass
def validate_email(email):
    """Check if email is exists"""
    if "@" not in email or "." not in email:
        raise ValidationError("Invalid email. Email must contain @ or .")
    return True

def validate_age(age):
    """Check if age is valid"""
    if not age .isdigit():
        raise ValidationError("Age must be a number!")
    age_int = int(age)
    if age_int < 0 or age_int > 120:
        raise ValidationError("Age must be between 0 and 120")
    return True
def validate_password(password):
    """Check if the password is valid"""
    if len(password) < 8:
        raise ValidationError("Password must be at least 8 characters long")
    if not any (c.isdigit() for c in password):
        raise validationError(" Password must contain at least one number")
    if not any (c.isupper() for c in password):
        raise ValidationError("Password must contain at least one capital letter")
    return True

# use validators
def register_user():
    try:
        email = input("Enter email: ")
        validate_email(email)

        age = input("Enter age: ")
        validate_age(age)

        password = input("Enter a password: ")
        validate_password(password)

        print("User registered successfully!")

        # save to file
        with open("user.txt", "a") as file:
            file.write(f"{email}, {age}\n")
    except ValidationError as e:
        print(f"Validation Error: {e}")
    except Exception as e:
        print(f" Error: {e}")
register_user()
