from case_MBPP_395 import count_vowels


def check(candidate):
    assert candidate('bestinstareels') == 7
    assert candidate('partofthejourneyistheend') == 12
    assert candidate('amazonprime') == 5

if __name__ == '__main__':
    check(count_vowels)