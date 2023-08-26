# Write a function that divides 2 integers and prints the result.
# Prototype: def safe_print_division(a, b):
# You can assume that a and b are integers
# The result of the division should print on the finally: section preceded by Inside result:
# Returns the value of the division, otherwise: None
# You have to use try: / except: / finally:
# You have to use "{}".format() to print the result
# You are not allowed to import any module


def safe_print_division(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("None")
    else:
        print("Inside result: {}".format(result))
    finally:
        return result if 'result' in locals() else None

# Test cases
print(safe_print_division(10, 5))  # Should print division result and return 2.0
print(safe_print_division(10, 0))  # Should print "None" and return None
