from case_MBPP_423 import max_run_uppercase


def check(candidate):
    assert candidate('GeMKSForGERksISBESt') == 5
    assert candidate('PrECIOusMOVemENTSYT') == 6
    assert candidate('GooGLEFluTTER') == 4

if __name__ == '__main__':
    check(max_run_uppercase)