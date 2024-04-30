from case_MBPP_338 import wind_chill


def check(candidate):
    assert candidate(120,35)==40
    assert candidate(40,20)==19
    assert candidate(10,8)==6

if __name__ == '__main__':
    check(wind_chill)