# Write a Python function called validate_password that takes a password as input and performs the following checks:

# The password should be at least 8 characters long.
# The password should contain at least one uppercase letter, one lowercase letter, and one digit.
# The password should not contain spaces.

# Prototype: def validate_password(password)

# Returns True if the password passes all the checks, and False otherwise.

# You are not allowed to import any module.

def validate_password(password):
    has_uppercase = False
    has_lowercase = False
    has_digit = False
    has_space = False
    
    for char in password:
        if char.isupper():
            has_uppercase = True
        elif char.islower():
            has_lowercase = True
        elif char.isdigit():
            has_digit = True
        elif char.isspace():
            has_space = True
            
    # Check if all conditions are met
    if has_uppercase and has_lowercase and has_digit and len(password) >= 8 and not has_space:
        return True
    else:
        return False