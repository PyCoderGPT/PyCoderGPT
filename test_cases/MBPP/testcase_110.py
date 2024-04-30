from case_MBPP_110 import replace_blank


def check(candidate):
    assert candidate("hello people",'@')==("hello@people")
    assert candidate("python program language",'$')==("python$program$language")
    assert candidate("blank space","-")==("blank-space")

if __name__ == '__main__':
    check(replace_blank)