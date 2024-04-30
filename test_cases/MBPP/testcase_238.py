from case_MBPP_238 import remove_whitespaces


def check(candidate):
    assert candidate(' Google    Flutter ') == 'GoogleFlutter'
    assert candidate(' Google    Dart ') == 'GoogleDart'
    assert candidate(' iOS    Swift ') == 'iOSSwift'

if __name__ == '__main__':
    check(remove_whitespaces)