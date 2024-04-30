from case_MBPP_363 import all_Characters_Same


def check(candidate):
    assert candidate("python") == False
    assert candidate("aaa") == True
    assert candidate("data") == False

if __name__ == '__main__':
    check(all_Characters_Same)