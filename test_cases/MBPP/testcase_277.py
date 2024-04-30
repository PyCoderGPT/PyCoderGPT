from case_MBPP_277 import empty_list


def check(candidate):
    assert candidate(5)==[{},{},{},{},{}]
    assert candidate(6)==[{},{},{},{},{},{}]
    assert candidate(7)==[{},{},{},{},{},{},{}]

if __name__ == '__main__':
    check(empty_list)