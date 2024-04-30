from case_MBPP_004 import find_char_long


def check(candidate):
    assert set(candidate('Please move back to stream')) == set(['Please', 'move', 'back', 'stream'])
    assert set(candidate('Jing Eco and Tech')) == set(['Jing', 'Tech'])
    assert set(candidate('Jhingai wulu road Zone 3')) == set(['Jhingai', 'wulu', 'road', 'Zone'])

if __name__ == '__main__':
    check(find_char_long)