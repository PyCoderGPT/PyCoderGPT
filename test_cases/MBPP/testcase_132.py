from case_MBPP_132 import swap_numbers


def check(candidate):
    assert candidate(10,20)==(20,10)
    assert candidate(15,17)==(17,15)
    assert candidate(100,200)==(200,100)

if __name__ == '__main__':
    check(swap_numbers)