from case_MBPP_359 import check_str


def check(candidate):
    assert candidate("annie")
    assert not candidate("dawood")
    assert candidate("Else")

if __name__ == '__main__':
    check(check_str)