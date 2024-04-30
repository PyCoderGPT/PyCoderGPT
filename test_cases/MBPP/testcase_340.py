from case_MBPP_340 import remove_parenthesis


def check(candidate):
    assert candidate(["python (chrome)"])==("python")
    assert candidate(["string(.abc)"])==("string")
    assert candidate(["alpha(num)"])==("alpha")

if __name__ == '__main__':
    check(remove_parenthesis)