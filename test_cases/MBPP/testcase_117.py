from case_MBPP_117 import get_total_number_of_sequences


def check(candidate):
    assert candidate(10, 4) == 4
    assert candidate(5, 2) == 6
    assert candidate(16, 3) == 84

if __name__ == '__main__':
    check(get_total_number_of_sequences)