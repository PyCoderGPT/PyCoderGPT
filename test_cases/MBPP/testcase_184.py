from case_MBPP_184 import get_max_sum 


def check(candidate):
    assert get_max_sum(60) == 106
    assert get_max_sum(10) == 12
    assert get_max_sum(2) == 2

if __name__ == '__main__':
    check(get_max_sum )