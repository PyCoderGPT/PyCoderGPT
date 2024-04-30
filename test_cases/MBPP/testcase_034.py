from case_MBPP_034 import word_len


def check(candidate):
    assert candidate("Hadoop") == False
    assert candidate("great") == True
    assert candidate("structure") == True

if __name__ == '__main__':
    check(word_len)