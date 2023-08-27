# Write a function that returns a tuple with the length of a string and its first character.
# Prototype: def multiple_returns(sentence):
# If the sentence is empty, the first character should be equal to None
# You are not allowed to import any module


def multiple_returns(sentence):
    length = len(sentence)
    if length > 0:
        print("Length: {:d} - First character: {}".format(length, sentence[0]))
    else:
        print("Length: {:d} - First character: {}".format(length, None))