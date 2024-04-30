from case_MBPP_174 import colon_tuplex


def check(candidate):
    assert candidate(("HELLO", 5, [], True) ,2,50)==("HELLO", 5, [50], True)
    assert candidate(("HELLO", 5, [], True) ,2,100)==(("HELLO", 5, [100],True))
    assert candidate(("HELLO", 5, [], True) ,2,500)==("HELLO", 5, [500], True)

if __name__ == '__main__':
    check(colon_tuplex)