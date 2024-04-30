from case_MBPP_208 import round_and_sum


def check(candidate):
    assert candidate([22.4, 4.0, -16.22, -9.10, 11.00, -12.22, 14.20, -5.20, 17.50])==243
    assert candidate([5,2,9,24.3,29])==345
    assert candidate([25.0,56.7,89.2])==513

if __name__ == '__main__':
    check(round_and_sum)