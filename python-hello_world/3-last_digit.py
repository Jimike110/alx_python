#!/usr/bin/python3
import random
number = -98

# Get the last digit of the number
last_digit = abs(number) % 10  # Extract the last digit using modulo

# Apply the original sign to the last digit
if number < 0:
    last_digit *= -1

# Determine the appropriate message based on the last digit
if last_digit > 5:
    message = "and is greater than 5"
elif last_digit == 0:
    message = "and is 0"
else:
    message = "and is less than 6 and not 0"

# Print the result
print("The string Last digit of", number, "is", last_digit, message)
