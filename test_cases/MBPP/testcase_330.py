from case_MBPP_330 import replace_spaces


def check(candidate):
    assert candidate("My Name is Dawood") == 'My%20Name%20is%20Dawood'
    assert candidate("I am a Programmer") == 'I%20am%20a%20Programmer'
    assert candidate("I love Coding") == 'I%20love%20Coding'

if __name__ == '__main__':
    check(replace_spaces)