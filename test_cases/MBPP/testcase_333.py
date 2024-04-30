from case_MBPP_333 import replace_spaces


def check(candidate):
    assert candidate('Jumanji The Jungle') == 'Jumanji_The_Jungle'
    assert candidate('The_Avengers') == 'The Avengers'
    assert candidate('Fast and Furious') == 'Fast_and_Furious'

if __name__ == '__main__':
    check(replace_spaces)