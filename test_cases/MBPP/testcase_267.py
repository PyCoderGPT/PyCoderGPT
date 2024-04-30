from case_MBPP_267 import toggle_string


def check(candidate):
    assert candidate("Python")==("pYTHON")
    assert candidate("Pangram")==("pANGRAM")
    assert candidate("LIttLE")==("liTTle")

if __name__ == '__main__':
    check(toggle_string)