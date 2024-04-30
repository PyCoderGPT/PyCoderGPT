from case_MBPP_290 import find_adverbs


def check(candidate):
    assert candidate("Clearly, he has no excuse for such behavior.") == '0-7: Clearly'
    assert candidate("Please handle the situation carefuly") == '28-36: carefuly'
    assert candidate("Complete the task quickly") == '18-25: quickly'

if __name__ == '__main__':
    check(find_adverbs)