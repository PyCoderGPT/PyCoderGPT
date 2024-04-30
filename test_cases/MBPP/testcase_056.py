from case_MBPP_056 import snake_to_camel


def check(candidate):
    assert candidate('python_program')=='PythonProgram'
    assert candidate('python_language')==('PythonLanguage')
    assert candidate('programming_language')==('ProgrammingLanguage')

if __name__ == '__main__':
    check(snake_to_camel)