from case_MBPP_201 import snake_to_camel


def check(candidate):
    assert candidate('android_tv') == 'AndroidTv'
    assert candidate('google_pixel') == 'GooglePixel'
    assert candidate('apple_watch') == 'AppleWatch'

if __name__ == '__main__':
    check(snake_to_camel)