from case_MBPP_243 import reverse_string_list


def check(candidate):
    assert candidate(['Red', 'Green', 'Blue', 'White', 'Black'])==['deR', 'neerG', 'eulB', 'etihW', 'kcalB']
    assert candidate(['john','amal','joel','george'])==['nhoj','lama','leoj','egroeg']
    assert candidate(['jack','john','mary'])==['kcaj','nhoj','yram']

if __name__ == '__main__':
    check(reverse_string_list)