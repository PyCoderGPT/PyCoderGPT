from case_MBPP_369 import lcs_of_three


def check(candidate):
    assert candidate('AGGT12', '12TXAYB', '12XBA') == 2
    assert candidate('Reels', 'Reelsfor', 'ReelsforReels') == 5
    assert candidate('abcd1e2', 'bc12ea', 'bd1ea') == 3

if __name__ == '__main__':
    check(lcs_of_three)