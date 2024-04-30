from case_MBPP_045 import find_substring


def check(candidate):
    assert candidate(["red", "black", "white", "green", "orange"],"ack")==True
    assert candidate(["red", "black", "white", "green", "orange"],"abc")==False
    assert candidate(["red", "black", "white", "green", "orange"],"ange")==True

if __name__ == '__main__':
    check(find_substring)