from case_MBPP_212 import extract_rear


def check(candidate):
    assert candidate(('Mers', 'for', 'Vers') ) == ['s', 'r', 's']
    assert candidate(('Avenge', 'for', 'People') ) == ['e', 'r', 'e']
    assert candidate(('Gotta', 'get', 'go') ) == ['a', 't', 'o']

if __name__ == '__main__':
    check(extract_rear)