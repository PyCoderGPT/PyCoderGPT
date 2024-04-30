from case_MBPP_304 import armstrong_number


def check(candidate):
    assert candidate(153)==True
    assert candidate(259)==False
    assert candidate(4458)==False

if __name__ == '__main__':
    check(armstrong_number)