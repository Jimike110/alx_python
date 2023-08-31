# Write a function that returns a key with the biggest integer value.
# Prototype: def best_score(a_dictionary):
# You can assume that all values are only integers
# If no score found, return None
# You can assume all students have a different score
# You are not allowed to import any module


def best_score(a_dictionary):
    scores_list = sorted(a_dictionary.values())
    if len(scores_list) > 0:
        return scores_list[-1]
    return None

        