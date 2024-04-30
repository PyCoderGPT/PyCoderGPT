from case_MBPP_348 import power_base_sum


def check(candidate):
    assert candidate(2,100)==115
    assert candidate(8,10)==37
    assert candidate(8,15)==62
    assert candidate(3,3)==9

if __name__ == '__main__':
    check(power_base_sum)