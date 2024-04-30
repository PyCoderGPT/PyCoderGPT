from case_HE_029 import filter_by_prefix


def check(candidate):
    assert candidate([], 'john') == []
    assert candidate(['xxx', 'asd', 'xxy', 'john doe', 'xxxAAA', 'xxx'], 'xxx') == ['xxx', 'xxxAAA', 'xxx']

if __name__ == '__main__':
    check(filter_by_prefix)