from case_MBPP_119 import count_charac


def check(candidate):
    assert candidate("python programming")==18
    assert candidate("language")==8
    assert candidate("words")==5

if __name__ == '__main__':
    check(count_charac)