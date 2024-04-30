from case_MBPP_107 import min_of_three


def check(candidate):
    assert candidate(10,20,0)==0
    assert candidate(19,15,18)==15
    assert candidate(-10,-20,-30)==-30

if __name__ == '__main__':
    check(min_of_three)