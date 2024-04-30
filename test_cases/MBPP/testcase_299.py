from case_MBPP_299 import removezero_ip


def check(candidate):
    assert candidate("216.08.094.196")==('216.8.94.196')
    assert candidate("12.01.024")==('12.1.24')
    assert candidate("216.08.094.0196")==('216.8.94.196')

if __name__ == '__main__':
    check(removezero_ip)