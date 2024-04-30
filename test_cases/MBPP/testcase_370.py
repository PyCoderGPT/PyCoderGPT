from case_MBPP_370 import capital_words_spaces


def check(candidate):
    assert candidate("Python") == 'Python'
    assert candidate("PythonProgrammingExamples") == 'Python Programming Examples'
    assert candidate("GetReadyToBeCodingFreak") == 'Get Ready To Be Coding Freak'

if __name__ == '__main__':
    check(capital_words_spaces)