from case_MBPP_272 import extract_values


def check(candidate):
    assert candidate('"Python", "PHP", "Java"')==['Python', 'PHP', 'Java']
    assert candidate('"python","program","language"')==['python','program','language']
    assert candidate('"red","blue","green","yellow"')==['red','blue','green','yellow']

if __name__ == '__main__':
    check(extract_values)