from case_MBPP_407 import new_tuple


def check(candidate):
    assert candidate(["WEB", "is"], "best") == ('WEB', 'is', 'best')
    assert candidate(["We", "are"], "Developers") == ('We', 'are', 'Developers')
    assert candidate(["Part", "is"], "Wrong") == ('Part', 'is', 'Wrong')

if __name__ == '__main__':
    check(new_tuple)