from case_MBPP_339 import sample_nam


def check(candidate):
    assert candidate(['sally', 'Dylan', 'rebecca', 'Diana', 'Joanne', 'keith'])==16
    assert candidate(["php", "res", "Python", "abcd", "Java", "aaa"])==10
    assert candidate(["abcd", "Python", "abba", "aba"])==6

if __name__ == '__main__':
    check(sample_nam)