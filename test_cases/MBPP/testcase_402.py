from case_MBPP_402 import rgb_to_hsv


def check(candidate):
    assert candidate(255, 255, 255)==(0, 0.0, 100.0)
    assert candidate(0, 215, 0)==(120.0, 100.0, 84.31372549019608)
    assert candidate(10, 215, 110)==(149.26829268292684, 95.34883720930233, 84.31372549019608)

if __name__ == '__main__':
    check(rgb_to_hsv)