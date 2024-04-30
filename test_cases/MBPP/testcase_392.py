from case_MBPP_392 import remove_length


def check(candidate):
    assert candidate('The person is most value tet', 3) == 'person is most value'
    assert candidate('If you told me about this ok', 4) == 'If you me about ok'
    assert candidate('Forces of darkeness is come into the play', 4) == 'Forces of darkeness is the'

if __name__ == '__main__':
    check(remove_length)