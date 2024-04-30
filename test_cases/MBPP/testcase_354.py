from case_MBPP_354 import replace_specialchar


def check(candidate):
    assert candidate('Python language, Programming language.')==('Python:language::Programming:language:')
    assert candidate('a b c,d e f')==('a:b:c:d:e:f')
    assert candidate('ram reshma,ram rahim')==('ram:reshma:ram:rahim')

if __name__ == '__main__':
    check(replace_specialchar)