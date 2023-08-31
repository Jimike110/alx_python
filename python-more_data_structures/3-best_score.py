# Write a function that returns a key with the biggest integer value.
# Prototype: def best_score(a_dictionary):
# You can assume that all values are only integers
# If no score found, return None
# You can assume all students have a different score
# You are not allowed to import any module


def best_score(a_dictionary):
    if a_dictionary is not None:  # Check if the dictionary is not None
        best_key = None
        max_score = float("-inf")
        all_values = list(a_dictionary.values())

        if len(all_values) > 0:
            for key, value in a_dictionary.items():
                if value > max_score:
                    max_score = value
                    best_key = key
            return best_key
    return None
    
