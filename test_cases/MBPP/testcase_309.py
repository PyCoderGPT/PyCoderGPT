from case_MBPP_309 import reverse_words


def check(candidate):
    assert candidate("python program")==("program python")
    assert candidate("java language")==("language java")
    assert candidate("indian man")==("man indian")

if __name__ == '__main__':
    check(reverse_words)