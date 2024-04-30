from case_MBPP_215 import change_date_format


def check(candidate):
    assert candidate("2026-01-02") == '02-01-2026'
    assert candidate("2020-11-13") == '13-11-2020'
    assert candidate("2021-04-26") == '26-04-2021'

if __name__ == '__main__':
    check(change_date_format)