from case_MBPP_237 import extract_string


def check(candidate):
    assert candidate(['Python', 'list', 'exercises', 'practice', 'solution'] ,8)==['practice', 'solution']
    assert candidate(['Python', 'list', 'exercises', 'practice', 'solution'] ,6)==['Python']
    assert candidate(['Python', 'list', 'exercises', 'practice', 'solution'] ,9)==['exercises']

if __name__ == '__main__':
    check(extract_string)