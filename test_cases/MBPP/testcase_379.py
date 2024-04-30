from case_MBPP_379 import count_reverse_pairs


def check(candidate):
    assert candidate(["julia", "best", "tseb", "for", "ailuj"])== 2
    assert candidate(["geeks", "best", "for", "skeeg"]) == 1
    assert candidate(["makes", "best", "sekam", "for", "rof"]) == 2

if __name__ == '__main__':
    check(count_reverse_pairs)