from case_MBPP_417 import remove_all_spaces


def check(candidate):
    assert candidate('python  program')==('pythonprogram')
    assert candidate('python   programming    language')==('pythonprogramminglanguage')
    assert candidate('python                     program')==('pythonprogram')
    assert candidate('   python                     program')=='pythonprogram'

if __name__ == '__main__':
    check(remove_all_spaces)