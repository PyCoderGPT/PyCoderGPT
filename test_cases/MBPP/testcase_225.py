from case_MBPP_225 import remove_odd


def check(candidate):
    assert candidate("python")==("yhn")
    assert candidate("program")==("rga")
    assert candidate("language")==("agae")

if __name__ == '__main__':
    check(remove_odd)