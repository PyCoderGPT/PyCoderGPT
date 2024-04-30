from case_MBPP_258 import replace_char


def check(candidate):
    assert candidate("polygon",'y','l')==("pollgon")
    assert candidate("character",'c','a')==("aharaater")
    assert candidate("python",'l','a')==("python")

if __name__ == '__main__':
    check(replace_char)