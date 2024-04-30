from case_MBPP_228 import find_adverb_position


def check(candidate):
    assert candidate("clearly!! we can see the sky")==(0, 7, 'clearly')
    assert candidate("seriously!! there are many roses")==(0, 9, 'seriously')
    assert candidate("unfortunately!! sita is going to home")==(0, 13, 'unfortunately')

if __name__ == '__main__':
    check(find_adverb_position)