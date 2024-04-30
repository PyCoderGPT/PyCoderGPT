from case_MBPP_288 import my_dict


def check(candidate):
    assert candidate({10})==False
    assert candidate({11})==False
    assert candidate({})==True

if __name__ == '__main__':
    check(my_dict)