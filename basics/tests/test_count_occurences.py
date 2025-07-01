from count_occurences import count_occurrence

def test_count_occurrence():
    input_str = "a lazy dog jumps over the sleeping wolf"
    expected = {
        'a': 1, ' ': 7, 'l': 3, 'z': 1, 'y': 1, 'd': 1, 'o': 2, 'g': 1, 'j': 1, 'u': 1,
        'm': 1, 'p': 1, 's': 2, 'v': 1, 'e': 3, 'r': 1, 't': 1, 'h': 1, 'n': 1, 'w': 1, 'f': 1, 'i': 1
    }
    assert count_occurrence(input_str) == expected
