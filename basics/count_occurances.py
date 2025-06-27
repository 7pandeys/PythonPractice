var = "a lazy dog jumps over the sleeping wolf"


def count_occurrence(var):
    occurrence = {}
    for character in var:
        if character in occurrence.keys() and character == " ":
            occurrence[character] = occurrence[character] + 1
        else:
            occurrence[character] = 1
    return occurrence


print(count_occurrence(var))
# output: {'a': 1, ' ': 7, 'l': 1, 'z': 1, 'y': 1, 'd': 1, 'o': 1, 'g': 1, 'j': 1, 'u': 1, 'm': 1, 'p': 1, 's': 1,
# 'v': 1, 'e': 1, 'r': 1, 't': 1, 'h': 1, 'i': 1, 'n': 1, 'w': 1, 'f': 1}
